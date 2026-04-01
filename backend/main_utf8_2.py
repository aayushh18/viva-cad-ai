import os
import uuid
import json
from datetime import datetime
from typing import List, Optional
from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import Session, select

from models import Design, Iteration, engine, create_db_and_tables
from AIPromptEngine import AIPromptEngine
from FreeCADAdapter import FreeCADAdapter

app = FastAPI(title="Viva CAD AI Production Backend")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize
create_db_and_tables()
prompt_engine = AIPromptEngine()
cad_adapter = FreeCADAdapter(output_dir="../data/output")

def get_db():
    with Session(engine) as session:
        yield session

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

@app.post("/designs/generate")
async def generate_design(prompt: str, db: Session = Depends(get_db)):
    try:
        # 1. Generate SJMS from Prompt
        schema = prompt_engine.generate_schema(prompt)
        
        # 2. Save to DB
        design = Design(
            prompt=prompt,
            schema_json=json.dumps(schema),
            status="DRAFT"
        )
        db.add(design)
        db.commit()
        db.refresh(design)
        
        return design
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/designs/{design_id}/build")
async def build_design(design_id: int, db: Session = Depends(get_db)):
    design = db.get(Design, design_id)
    if not design:
        raise HTTPException(status_code=404, detail="Design not found")
    
    schema = json.loads(design.schema_json)
    build_id = str(uuid.uuid4().hex)[:8]
    output_base = f"../data/output/design_{design_id}_{build_id}"
    
    # 1. Generate Script
    script_content = cad_adapter.generate_script(schema, output_base)
    script_path = f"{output_base}.py"
    with open(script_path, "w") as f:
        f.write(script_content)
    
    # 2. Execute
    result = cad_adapter.execute_script(script_path)
    
    # 3. Record Iteration
    version = len(db.exec(select(Iteration).where(Iteration.design_id == design_id)).all()) + 1
    iteration = Iteration(
        design_id=design_id,
        version=version,
        python_script=script_content,
        error_log=result.get("error"),
        file_path=f"{output_base}.FCStd" if result["success"] else None
    )
    db.add(iteration)
    
    if result["success"]:
        design.status = "APPROVED"
    else:
        design.status = "FAILED"
    
    db.commit()
    db.refresh(design)
    
    return {"design": design, "iteration": iteration, "success": result["success"]}

@app.get("/designs")
async def list_designs(db: Session = Depends(get_db)):
    return db.exec(select(Design)).all()

@app.get("/designs/{design_id}/iterations")
async def list_iterations(design_id: int, db: Session = Depends(get_db)):
    return db.exec(select(Iteration).where(Iteration.design_id == design_id)).all()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

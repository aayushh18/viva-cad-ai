import os
import uuid
import json
from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel
from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
import os
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

class DesignUpdate(BaseModel):
    python_script: str

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

@app.post("/designs/generate")
def generate_design(prompt: str, db: Session = Depends(get_db)):
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
def build_design(design_id: int, headless: bool = True, db: Session = Depends(get_db)):
    design = db.get(Design, design_id)
    if not design:
        raise HTTPException(status_code=404, detail="Design not found")
    
    schema = json.loads(design.schema_json)
    build_id = str(uuid.uuid4().hex)[:8]
    output_base = f"../data/output/design_{design_id}_{build_id}"
    
    # 1. Generate Script
    script_content = schema.get("python_script", "")
    script_content = script_content.replace('"output.step"', f'"{output_base}.step"').replace("'output.step'", f"'{output_base}.step'")
    
    visual_append = """
import FreeCAD
import Part

try:
    if 'result' in locals() and result is not None:
        try:
            Part.show(result)
        except Exception:
            pass
            
    if 'doc' in locals() and doc is not None:
        doc.recompute()
        
    if FreeCAD.GuiUp:
        import FreeCADGui as Gui
        if Gui.ActiveDocument and Gui.ActiveDocument.ActiveView:
            Gui.ActiveDocument.ActiveView.viewIsometric()
            Gui.SendMsgToActiveView("ViewFit")
except Exception:
    pass
"""
    if "Part.show" not in script_content and "FreeCAD.GuiUp" not in script_content:
        script_content += "\n" + visual_append

    export_append = f"""
try:
    import Part
    import FreeCAD as App
    doc = App.ActiveDocument
    if doc:
        objs = [obj for obj in doc.Objects if hasattr(obj, 'Shape') and obj.Shape is not None]
        if objs:
            Part.export(objs, r'{output_base}.step')
        doc.saveAs(r'{output_base}.FCStd')
except Exception as e:
    print("Export Failed:", e)
"""
    script_content += "\n" + export_append
    
    # Syntax validation layer
    try:
        compile(script_content, '<string>', 'exec')
    except SyntaxError as e:
        raise ValueError(f"AI generated invalid Python syntax: {e}")
        
    script_path = f"{output_base}.py"
    with open(script_path, "w") as f:
        f.write(script_content)
    
    # 2. Execute
    result = cad_adapter.execute_script(script_path, headless=headless)
    
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
        # VALIDATION: Verify STEP file size > 0
        step_file = f"{output_base}.step"
        if os.path.exists(step_file) and os.path.getsize(step_file) > 0:
            design.status = "APPROVED"
        else:
            design.status = "FAILED"
            result["success"] = False
            if "error" not in result:
                result["error"] = "Validation Error: STEP file was not created or is empty. (Size 0)"
    else:
        design.status = "FAILED"
    
    db.commit()
    db.refresh(design)
    
    return {"design": design, "iteration": iteration, "success": result["success"]}

@app.put("/designs/{design_id}")
async def update_design_script(design_id: int, req: DesignUpdate, db: Session = Depends(get_db)):
    design = db.get(Design, design_id)
    if not design:
        raise HTTPException(status_code=404, detail="Design not found")
    
    schema = json.loads(design.schema_json)
    schema["python_script"] = req.python_script
    design.schema_json = json.dumps(schema)
    db.commit()
    db.refresh(design)
    return design

@app.get("/designs")
async def list_designs(db: Session = Depends(get_db)):
    # Return designs in descending order to show newest first!
    designs = db.exec(select(Design).order_by(Design.id.desc())).all()
    return designs

@app.get("/designs/{design_id}/iterations")
async def list_iterations(design_id: int, db: Session = Depends(get_db)):
    return db.exec(select(Iteration).where(Iteration.design_id == design_id)).all()

@app.delete("/designs/{design_id}")
async def delete_design(design_id: int, db: Session = Depends(get_db)):
    design = db.get(Design, design_id)
    if not design:
        raise HTTPException(status_code=404, detail="Design not found")
    
    iterations = db.exec(select(Iteration).where(Iteration.design_id == design_id)).all()
    for it in iterations:
        db.delete(it)
        
    db.delete(design)
    db.commit()
    return {"message": f"Design {design_id} deleted"}

@app.delete("/designs")
async def clear_all_designs(db: Session = Depends(get_db)):
    iterations = db.exec(select(Iteration)).all()
    for it in iterations:
        db.delete(it)
        
    designs = db.exec(select(Design)).all()
    for d in designs:
        db.delete(d)
        
    db.commit()
    return {"message": "All designs cleared"}

@app.get("/download")
async def download_file(file: str):
    if not os.path.exists(file):
        raise HTTPException(status_code=404, detail="File not found")
    filename = os.path.basename(file)
    return FileResponse(file, media_type='application/octet-stream', filename=filename)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

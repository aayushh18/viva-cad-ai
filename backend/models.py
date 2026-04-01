from datetime import datetime
from typing import Optional
from sqlmodel import SQLModel, Field, create_engine, Session

class Design(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    prompt: str
    schema_json: str  # JSON string of SJMS
    status: str  # DRAFT, APPROVED, FAILED, REGENERATING
    created_at: datetime = Field(default_factory=datetime.utcnow)

class Iteration(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    design_id: int = Field(foreign_key="design.id")
    version: int
    python_script: str
    error_log: Optional[str] = None
    file_path: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)

sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url, echo=False)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session

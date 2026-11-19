from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text

from app.database import get_db
from app.models import User, Provider, RepairRequest, RepairImage, Application, Review
app = FastAPI()

@app.get("/api/health")
def health_check(db: Session = Depends(get_db)):
    db.execute(text("SELECT 1"))

    return {
        "status": "healthy",
        "database": "connected"
    }

@app.get("/api/repairs")
def get_repairs(db: Session = Depends(get_db)):
    repairs = db.query(RepairRequest).all()
    return repairs
from app.database import Base, engine

from app.models.user import User
from app.models.provider import Provider
from app.models.repair_request import RepairRequest


Base.metadata.create_all(bind=engine)

print("Database tables created successfully!")
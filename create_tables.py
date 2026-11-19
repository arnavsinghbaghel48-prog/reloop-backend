from app.database import Base, engine

from app.models.user import User
from app.models.provider import Provider 
from app.models.repair_request import RepairRequest
from app.models.repair_image import RepairImage
from app.models.application import Application


Base.metadata.create_all(bind=engine)

print("Database tables created successfully!")
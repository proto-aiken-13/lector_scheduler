# backend/app/models/lector.py
from sqlalchemy import Column, Integer, String, Boolean
from app.database import Base

class Lector(Base):
    __tablename__ = "lectors"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    active = Column(Boolean, default=True)
    phone = Column(String, default=None)

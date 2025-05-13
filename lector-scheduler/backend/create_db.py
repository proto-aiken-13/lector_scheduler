# backend/create_db.py
from app.database import Base, engine
from app.models.lector import Lector

# Create all tables defined by Base subclasses
Base.metadata.create_all(bind=engine)

print("Database and tables created.")

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from infrastructure.adapters.database.models import Base

class DatabaseConfig:
    def __init__(self, connection_string: str):
        self.engine = create_engine(connection_string)
        self.SessionLocal = sessionmaker(bind=self.engine)
    
    def create_database(self):
        Base.metadata.create_all(bind=self.engine)
    
    def get_db(self):
        return self.SessionLocal()

from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./parsed_data.db"

Base = declarative_base()


class ParsedData(Base):
    __tablename__ = "parsed_data"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    price = Column(String)
    parsed_date = Column(DateTime, default=datetime.utcnow)


def get_db():
    engine = create_engine(SQLALCHEMY_DATABASE_URL)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    Base.metadata.create_all(bind=engine)

    return SessionLocal()

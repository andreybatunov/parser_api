from fastapi import FastAPI, HTTPException
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from pydantic import BaseModel
import asyncio
from parser import Parser


app = FastAPI()


SQLALCHEMY_DATABASE_URL = "sqlite:///./parsed_data.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


class ParsedData(Base):
    __tablename__ = "parsed_data"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    price = Column(String)
    parsed_date = Column(DateTime, default=datetime.utcnow)


class DataSchema(BaseModel):
    name: str
    price: str

    class Config:
        orm_mode = True


Base.metadata.create_all(bind=engine)


async def parse_website():
    try:
        site_config = "SDVOR" # "HENDERSON" или "SDVOR"
        parser = Parser(site_config)
        products = parser.get_products()
        db = SessionLocal()
        for product in products:
            data = {
                "name": product['name'],
                "price": product['price']
            }

            existing_item = db.query(ParsedData).filter(
                ParsedData.name == data['name'],
                ParsedData.price == data['price']
            ).first()
            
            if not existing_item:
                db_item = ParsedData(**data)
                db.add(db_item)
                db.commit()

        db.close()
        
    except Exception as e:
        print(f"Ошибка при парсинге: {str(e)}")


@app.get("/data/")
async def get_all_data():
    db = SessionLocal()
    items = db.query(ParsedData).all()
    db.close()
    return items

@app.get("/data/{item_id}")
async def get_data(item_id: int):
    db = SessionLocal()
    item = db.query(ParsedData).filter(ParsedData.id == item_id).first()
    db.close()
    if not item:
        raise HTTPException(status_code=404, detail="Данные не найдены")
    return item

@app.put("/data/{item_id}")
async def update_data(item_id: int, data: DataSchema):
    db = SessionLocal()
    item = db.query(ParsedData).filter(ParsedData.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Данные не найдены")
    
    for key, value in data.dict().items():
        setattr(item, key, value)
    
    db.commit()
    db.close()
    return item

@app.delete("/data/{item_id}")
async def delete_data(item_id: int):
    db = SessionLocal()
    item = db.query(ParsedData).filter(ParsedData.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Данные не найдены")
    
    db.delete(item)
    db.commit()
    db.close()
    return {"message": "Данные успешно удалены"}


@app.on_event("startup")
async def start_parser():
    asyncio.create_task(run_parser())


async def run_parser():
    while True:
        await parse_website()
        await asyncio.sleep(3600)

# uvicorn API_PARSER:app --reload
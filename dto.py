from pydantic import BaseModel


class DataSchemaIn(BaseModel):
    name: str
    price: str


class DataSchemaOut(BaseModel):
    id: int
    name: str
    price: str

    class Config:
        orm_mode = True

    def __str__(self):
        return f"ID: {self.id}, \n Name: {self.name}, \n Price: {self.price}"

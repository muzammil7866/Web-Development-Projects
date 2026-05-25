from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

#Defining the Request Body Model
class item(BaseModel):
    name: str
    price: float
    in_stock: bool


#Accept a POST request with json body
@app.post("/create-item")
def create_item(item:item):
    return {"name": item.name, "price": item.price, "in_stock": item.in_stock}

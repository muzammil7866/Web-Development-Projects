from fastapi import FastAPI
from pydantic import BaseModel #pydantic not uvicorn

app = FastAPI()

@app.get("/")
def get_root():
    return {"message": "root accessed successfully"}

class NameRequest(BaseModel):
    name: str #careful


@app.post("/greet") #post careful
def greet_user(data: NameRequest): #parameters careful
    return {"message": f"Hello {data.name}! Welcome to FastAPI."} #dictionary

from fastapi import FastAPI

app = FastAPI()

#query parameters
@app.get("/products/")
def list_products(skip: int = 0, limit: int = 10):
    return {"skip": skip, "limit": limit}

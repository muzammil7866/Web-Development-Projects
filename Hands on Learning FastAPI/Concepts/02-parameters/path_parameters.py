from fastapi import FastAPI

app = FastAPI()

#path parameters
@app.get("/items/{item_id}")
def read_item(item_id: int):
	return {"item_id": item_id}

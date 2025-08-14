from fastapi import FastAPI
from mangum import Mangum
app = FastAPI()
@app.get("/api")
def read_root():
    return {"message": "Hola desde FastAPI en Lambda!"}

@app.get("/api/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id, "description": "Este es un item de ejemplo"}

# El adaptador Mangum que permite a API Gateway comunicarse con FastAPI
handler = Mangum(app)


from fastapi import FastAPI
from app.routers import router
import uvicorn

app = FastAPI()
app.include_router(router=router)

@app.get("/")
def hello_world():
    return {"Success": "Hello Word"}
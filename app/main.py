from fastapi import FastAPI
from app.backend.db import create_db_and_tables

from app.routes import accounts

app = FastAPI()


@app.on_event("startup")
def on_startup():
    create_db_and_tables()


app.include_router(accounts.router)


@app.get('/')
async def hello_world():
    return {"details": "Hello World"}

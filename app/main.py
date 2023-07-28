from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.backend.db import create_db_and_tables

from app.routes import accounts

origins = ['*']

app = FastAPI()

app.add_middleware(
  CORSMiddleware,
  allow_origins=origins,
  allow_credentials=True,
  allow_methods=['*'],
  allow_headers=['*'],
)


@app.on_event("startup")
def on_startup():
    create_db_and_tables()


app.include_router(accounts.router)


@app.get('/')
async def hello_world():
    return {"details": "Hello World"}

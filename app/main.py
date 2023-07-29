from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
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


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(
        request, exc):
    # return PlainTextResponse(str(exc), status_code=400)
    return JSONResponse(
        status_code=400,
        content={"message": str(exc)}
    )


@app.on_event("startup")
def on_startup():
    create_db_and_tables()


app.include_router(accounts.router)


@app.get('/')
async def hello_world():
    return {"details": "Hello World"}

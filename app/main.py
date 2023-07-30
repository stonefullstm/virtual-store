from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from fastapi.openapi.utils import get_openapi
from app.backend.db import create_db_and_tables

from app.routes import accounts

origins = ['*']

app = FastAPI(
    title="Virtual Store API",
    description="This API implements store transaction system.",
    version="1.0.0",
    )


def custom_openapi():
    if not app.openapi_schema:
        app.openapi_schema = get_openapi(
            title=app.title,
            version=app.version,
            openapi_version=app.openapi_version,
            description=app.description,
            terms_of_service=app.terms_of_service,
            contact=app.contact,
            license_info=app.license_info,
            routes=app.routes,
            tags=app.openapi_tags,
            servers=app.servers,
        )
        for _, method_item in app.openapi_schema.get('paths').items():
            for _, param in method_item.items():
                responses = param.get('responses')
                # remove 422 response, also can remove other status code
                if '422' in responses:
                    del responses['422']
    return app.openapi_schema


app.openapi = custom_openapi


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

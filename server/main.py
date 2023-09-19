#!/usr/bin/env python3


from fastapi import FastAPI, APIRouter
from starlette.responses import JSONResponse
from server.api.router import api_router
# from server.exception_handlers.generic_exception_handlers import problem_detail_handler
# from pydantic_forms.exception_handlers.fastapi import form_error_handler

# api_router = APIRouter()

app = FastAPI(
    title="Pydantic FastAPI POC",
    description="testing pydantic2 forms",
    openapi_url="/v1/openapi.json",
    docs_url="/v1/docs",
    redoc_url="/v1/redoc",
    default_response_class=JSONResponse,
    # root_path="/backend",
    servers=[
        {"url": "/"},
    ],
)

app.include_router(api_router, prefix="/v1")


# app.add_exception_handler(FormException, form_error_handler)
# app.add_exception_handler(ProblemDetailException, problem_detail_handler)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


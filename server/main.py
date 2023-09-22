#!/usr/bin/env python3


from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from pydantic_forms.exception_handlers.fastapi import form_error_handler
from pydantic_forms.exceptions import FormException
from starlette.responses import JSONResponse

from server.api.error_handling import ProblemDetailException
from server.api.router import api_router
from server.exception_handlers.generic_exception_handlers import problem_detail_handler

app = FastAPI(
    title="Pydantic FastAPI POC",
    description="testing pydantic2 forms",
    openapi_url="/v1/openapi.json",
    docs_url="/v1/docs",
    redoc_url="/v1/redoc",
    default_response_class=JSONResponse,
    servers=[
        {"url": "/"},
    ],
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix="/v1")
app.add_exception_handler(FormException, form_error_handler)
app.add_exception_handler(ProblemDetailException, problem_detail_handler)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


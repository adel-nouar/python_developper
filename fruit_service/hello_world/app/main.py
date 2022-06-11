from http import HTTPStatus
from fastapi import FastAPI

from app.routers import hello

app = FastAPI(
    title='Hellooooo Wooorld',
    version='1.0.0',
    description='Get hello world here',
    root_path=''
)

app.include_router(hello.router)

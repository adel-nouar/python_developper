import logging
from http import HTTPStatus
from fastapi import FastAPI

from app.routers import hello

logging.basicConfig(encoding='utf-8', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

logger = logging.getLogger(__name__)

app = FastAPI(
    title='Hellooooo Wooorld',
    version='1.0.0',
    description='Get hello world here',
    root_path=''
)

app.include_router(hello.router)

from http import HTTPStatus
from fastapi import FastAPI

from app.routers import order

app = FastAPI(
    title='Your Fruit Self Service',
    version='1.0.0',
    description='Order your fruits here',
    root_path=''
)

app.include_router(order.router)


@app.get('/', status_code=HTTPStatus.OK)
async def root():
    """
    Endpoint for basic connectivity test.
    """
    return {'message': 'I am alive'}

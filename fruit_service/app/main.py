import logging
from http import HTTPStatus
from fastapi import FastAPI

from app.routers import order

logging.basicConfig(encoding='utf-8', level=logging.WARNING, format='%(asctime)s - %(levelname)s - %(message)s')

logger = logging.getLogger(__file__)


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
    logger.info('root called')
    return {'message': 'I am alive'}

import logging

from http import HTTPStatus
from fastapi import APIRouter

logger = logging.getLogger(__file__)
router = APIRouter(tags=['income'])

@router.get('/', status_code=HTTPStatus.OK)
async def root():
    logger.info('root called')
    return {'message': 'Hello World!'}
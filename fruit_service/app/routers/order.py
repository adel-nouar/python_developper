import logging
from http import HTTPStatus
from fastapi import APIRouter

logger = logging.getLogger(__file__)
router = APIRouter(tags=['income'])


@router.post('/order', status_code=HTTPStatus.OK)
async def order_call(order: str):
    logger.info(f'Incoming order: {order}')
    return {'order': order}

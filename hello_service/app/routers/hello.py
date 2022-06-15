import logging
from http import HTTPStatus
from typing import Dict

from fastapi import APIRouter

logger = logging.getLogger(__file__)
router = APIRouter(tags=['income'])


@router.post('/hello', status_code=HTTPStatus.OK)
async def hello_call(hello: str) -> Dict[str, str]:
    logger.info(f'Incoming hello: {hello}')
    return {'hello': hello}

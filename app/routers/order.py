from http import HTTPStatus
from fastapi import APIRouter

router = APIRouter(tags=['income'])


@router.post('/order', status_code=HTTPStatus.OK)
async def order_call(order: str):
    print(f'Incoming order: {order}')
    return {'order': order}

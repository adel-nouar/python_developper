from http import HTTPStatus
from fastapi import APIRouter

router = APIRouter(tags=['income'])

@router.get('/', status_code=HTTPStatus.OK)
async def root():
    return {'message': 'Hello World!'}
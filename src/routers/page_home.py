from fastapi import APIRouter


router = APIRouter()
@router.get('/')
@router.get('/home')
async def func_home():
    return {'message': "Hello. This is Hogan's backend!"}

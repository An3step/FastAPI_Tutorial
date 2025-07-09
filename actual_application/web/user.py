import os
from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from model.user import User
from error.Web_Exceptions import Missing, Duplicate
from datetime import timedelta

if os.getenv("CRYPTID_UNIT_TEST"):
    from fake import user as service
else:
    from service import user as service

ACCESS_TOKEN_EXPIRE_MINUTES = 30

router = APIRouter(prefix='/user')

oauth2_dependency = OAuth2PasswordBearer(tokenUrl='token')

def unauthorized():
    raise HTTPException(status_code=401,
                        detail='Incorrect username or password',
                        headers={"WWW-Authentificate": "Bearer"})

@router.post('/token')
async def create_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    """Получение имени пользователя, пароля из формы OAuth, возврат токена доступа"""
    user = service.auth_user(form_data.username, form_data.password)
    if not user:
        unauthorized()
    expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = service.create_access_token(data={'username': user.username}, expires=expires)
    return {"access_token": access_token, "token_type": "bearer"}

@router.get('/token')
def get_access_token(token: str = Depends(oauth2_dependency))->dict:
    """Возвращение текужещего токена доступа"""
    return {"token": token}

# ------------- CRUD

@router.get('/')
def get_all()->list[User]:
    return service.get_all()

@router.get('/{name}')
def get_one(name)-> User:
    try:
        return service.get_one(name)
    except Missing as missing_name:
        raise HTTPException(status_code=404, detail=missing_name.msg)
    
@router.post('/', status_code=201)
def create(user: User) -> User:
    try:
        return service.create(user)
    except Duplicate as duplicate_username:
        raise HTTPException(status_code=409, detail=duplicate_username.msg)

@router.patch('/')
def modify(name: str, user: User) -> User:
    try:
        return service.modify(name, user)
    except Missing as missing_name:
        raise HTTPException(status_code=404, detail=missing_name.msg)
    
@router.delete('/{name}')
def delete(name: str) -> None:
    try:
        return service.delete(name)
    except Missing as missing_name:
        raise HTTPException(status_code=404, detail=missing_name.msg)
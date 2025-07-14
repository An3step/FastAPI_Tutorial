from datetime import timedelta, datetime
import os
from jose import jwt
from model.user import User
from error.Web_Exceptions import Missing, Duplicate

if os.getenv('CRYPTID_UNIT_TEST'):
    from fake import user as data
else:
    from data import user as data

from passlib.context import CryptContext

SECRET_KEY = 'keep-it-secret-and-safe'
ALGORITHM = 'HS256'
pwd_content = CryptContext(schemes=['bcrypt'], deprecated='auto')

def verify_password(plain: str, hash: str) -> bool:
    """хеширование строки <plain> и сравнение с записью из базы данных"""
    return pwd_content.verify(plain, hash)

def get_hash(plain: str) -> str:
    """возвращение хеша строки <plain>"""
    return pwd_content.hash(plain)

def lookup_user(username: str) -> User | None:
    """Возврат пользователя из базы данных по имени username"""
    try:
        return data.get_one(username)
    except Missing:
        return None

def get_jwt_username(token: str) -> str | None:
    """возвращение имени пользователя из JWT-доступа <token>"""
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        if (username := payload.get('username')):
            return username
        return None
    except jwt.JWTError:
        return None

def get_current_user(token: str)-> User | None:
    """Декодирование токена <token> доступа OAuth и возврат объекта User"""
    username = get_jwt_username(token)
    if not username:
        return None
    user = lookup_user(username)
    return user if user else None

def auth_user(name: str, plain: str) -> User | None:
    """Аутентификация пользователя по имени и паролю"""
    user = lookup_user(name)
    if not user:
        return None
    return user if verify_password(plain, user.hashed_password) else None

def create_access_token(data: dict, expires: timedelta | None = None):
    """Возврат токена доступа JWT"""
    src = data.copy()
    now = datetime.now()
    if not expires:
        expires = timedelta(minutes=15)
    src.update({'exp': now + expires})
    encoded_jwt = jwt.encode(src, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

# ---------- CRUD

def get_all()->list[User]:
    return data.get_all()

def get_one(name)->User:
    return data.get_one(name)

def create(user: User)->User:
    return data.create(user)

def modify(name: str, user: User) -> User:
    return data.modify(name, user)

def delete(name: str) -> None:
    return data.delete(name)
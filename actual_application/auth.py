from fastapi import Depends, FastAPI, Header, Query, HTTPException
from fastapi.security import HTTPBasicCredentials, HTTPBasic

app = FastAPI()

basic = HTTPBasic()

secret_user : str = 'secret_user'
secret_password : str = 'loyalty'

@app.get("/who")
def get_user(creds: HTTPBasicCredentials = Depends(basic)):
    if creds.username == secret_user and creds.password == secret_password:
        return {"username": secret_user, "password": secret_password}
    raise HTTPException(401, detail='Cringe?')

@app.get('/')
def get_test(who: str = Header(), who2: str = Query()):
    return f'{who =}, {who2 =}'
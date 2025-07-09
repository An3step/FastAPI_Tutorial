from fastapi import FastAPI, Depends, params

app = FastAPI()

def user_dependency(name: str = params, password: str = params)->dict:
    return {"name": name, "password": password}

@app.get('/hello')
def get_user(user: dict = Depends(user_dependency)) -> dict:
    return user
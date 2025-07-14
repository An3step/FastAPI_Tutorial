from pathlib import Path
from fastapi import FastAPI, Form, Request
from fastapi.templating import Jinja2Templates

app = FastAPI()

top = Path(__file__).resolve().parent

template_obj = Jinja2Templates(directory=f'{top}/template')

from fake.creature import creatures
from fake.explorer import explorers

@app.get('/who2')
def greet2(name: str = Form()):
    return f'Hello, {name}'

@app.post('/who2')
def greet(name: str = Form()):
    return f'Hello, {name}'

@app.get('/list')
def show_list(request: Request):
    return template_obj.TemplateResponse('list.html',
                                         {'request': request,
                                          'explorers': explorers,
                                          'creatures': creatures})
from fastapi import FastAPI, Body, Header, Response, Depends, params
from .model import creature
from .web import explorer
import asyncio
import time

app = FastAPI()

app.include_router(explorer.router)

@app.get('/')
def default():
    return "hello"

@app.get('/hi')
def greet(who):
    time.sleep(10)
    return f"Hello? Are You? {who}"

@app.get('/creature')
def get_creatures()->list[creature.Creature]:
    return creature.get_Creatures()

# @app.post('/hi')
# def greet(who = Body(), who2 = Body()) :
#     return f'Hello? {who}, {who2}'


@app.post('/hi')
def greet(r: Response, who:str = Header(), connection=Header(default="keep-alive?"), who_bod=Body(embed=True)):
    r.headers["custom_header"] = "custom_content"
    return f"Hello? Are You? {who}, connection = {connection}, body_content={who_bod}?"
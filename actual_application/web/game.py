from pathlib import Path
from fastapi import APIRouter, Body, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pathlib import Path
from service import game as service

router = APIRouter(prefix='/game')

@router.get('')
def game_start(request: Request):
    word = service.get_word()
    top = Path(__file__).resolve().parents[1]
    templates = Jinja2Templates(directory=f'{top}/template')
    return templates.TemplateResponse('game.html', {'request': request, 'word': word})

@router.post('')
async def game_step(word: str = Body(), guess: str = Body()):
    score = service.get_score(word, guess)
    print(f'{word=}', f'{score=}')
    return score
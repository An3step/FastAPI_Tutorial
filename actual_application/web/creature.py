import os
from fastapi import APIRouter, HTTPException, Response
from model.creature import Creature
from error.Web_Exceptions import Duplicate, Missing
from collections import Counter
import matplotlib.pyplot as plt
import io

plt.switch_backend('Agg')

if os.getenv('CRYPTID_UNIT_TEST'):
    from fake import creature as service
else:
    from service import creature as service

router = APIRouter(prefix="/creature")

@router.get('/plot')
def plot():
    creatures = service.get_all()
    letters = 'ABCDEFGHJKLMNOPQRSTUVWXYZ'
    counts = Counter(creature.name[0] for creature in creatures)
    plt.figure(figsize=(10, 6))
    heights = {letter : counts.get(letter, 0) for letter in letters}
    bars = plt.bar(x = list(heights.keys()),
                   height=list(heights.values()))
    plt.title('Creature Names Frequency')
    plt.xlabel('Initial', fontsize=10)
    plt.ylabel('Frequency', fontsize=10)
    plt.tight_layout()
    png_buffer = io.BytesIO()
    plt.savefig(png_buffer, format='png')
    plt.clf()
    plt.close()

    png_data = png_buffer.getvalue()
    png_buffer.close()

    return Response(content=png_data, media_type="image/png")

@router.get('/')
def get_all() -> list[Creature]:
    """Получить всех существ"""
    return service.get_all()

@router.get('/{name}')
def get_one(name: str) -> Creature | None:
    """Получить одно существо по имени"""
    try:
        return service.get_one(name)
    except Missing as mis_name:
        raise HTTPException(status_code=404, detail=mis_name.msg)

@router.post('/', status_code=201)
def create(creature: Creature) -> Creature:
    try:
        return service.create(creature)
    except Duplicate as dupl_name:
        raise HTTPException(status_code=404, detail=dupl_name.msg)

@router.patch('/')
def modify(name: str, creature: Creature) -> Creature:
    try:
        return service.modify(name, creature)
    except Missing as mis_name:
        raise HTTPException(status_code=404, detail=mis_name.msg)

@router.put('/')
def replace(name: str, creature: Creature) -> Creature:
    try:
        return service.replace(name, creature)
    except Missing as mis_name:
        raise HTTPException(status_code=404, detail=mis_name.msg)


@router.delete('/{name}')
def delete(name: str):
    try:
        return service.delete(name)
    except Missing as mis_name:
        raise HTTPException(status_code=404, detail=mis_name.msg)
    



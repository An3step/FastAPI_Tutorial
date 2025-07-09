from fastapi import APIRouter, HTTPException
from model.creature import Creature
import service.creature as service
from error.Web_Exceptions import Duplicate, Missing

router = APIRouter(prefix="/creature")

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

@router.post('/')
def create(creature: Creature) -> Creature:
    try:
        return service.create(creature)
    except Duplicate as dupl_name:
        raise HTTPException(status_code=404, detail=dupl_name.msg)

@router.patch('/')
def modify(creature: Creature) -> Creature:
    try:
        return service.modify(creature)
    except Missing as mis_name:
        raise HTTPException(status_code=404, detail=mis_name.msg)

@router.put('/')
def replace(creature: Creature) -> Creature:
    try:
        return service.replace(creature)
    except Missing as mis_name:
        raise HTTPException(status_code=404, detail=mis_name.msg)


@router.delete('/{name}')
def delete(name: str):
    try:
        return service.delete(name)
    except Missing as mis_name:
        raise HTTPException(status_code=404, detail=mis_name.msg)

from fastapi import APIRouter, HTTPException
from model.explorer import Explorer
import service.explorer as service
from error.Web_Exceptions import Duplicate, Missing

router = APIRouter(prefix="/explorer")

@router.get('/')
def get_all() -> list[Explorer]:
    return service.get_all()

@router.get('/{name}')
def get_one(name: str)->Explorer:
    try:
        return service.get_one(name)
    except Missing as mis_name:
        raise HTTPException(status_code=404, detail=mis_name.msg)

@router.post('/')
def create(explorer: Explorer)->Explorer:
    try:
        return service.create(explorer)
    except Duplicate as dupl_name:
        raise HTTPException(status_code=404, detail=dupl_name.msg)


@router.patch('/')
def modify(name: str, explorer: Explorer)->Explorer:
    try:
        return service.modify(name, explorer)
    except Missing as mis_name:
        raise HTTPException(status_code=404, detail=mis_name.msg)

@router.put('/')
def replace(name: str, explorer: Explorer)->Explorer:
    try:
        return service.replace(name, explorer)
    except Missing as mis_name:
        raise HTTPException(status_code=404, detail=mis_name.msg)

@router.delete('/{name}')
def delete(name: str):
    try:
        return service.delete(name)
    except Missing as mis_name:
        raise HTTPException(status_code=404, detail=mis_name.msg)

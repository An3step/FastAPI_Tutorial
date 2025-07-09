from model.creature import Creature
import data.creature as data

def get_all() -> list[Creature]:
    """Возвращает всех существ из списка."""
    return data.get_all()

def get_one(name: str) -> Creature | None:
    return data.get_one(name)

def create(creature: Creature) -> Creature:
    """Добавляет новое существо в список и возвращает его."""
    return data.create(creature)

def modify(creature: Creature) -> Creature:
    return data.modify(creature)

def replace(creature: Creature) -> Creature:
    return data.modify(creature)

def delete(name: str)->Creature:
    return data.delete(name)
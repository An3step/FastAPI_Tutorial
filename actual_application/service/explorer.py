from model.explorer import Explorer
import data.explorer as data

def get_all() -> list[Explorer]:
    """Возвращает всех существ из списка."""
    return data.get_all()

def get_one(name: str) -> Explorer:
    return data.get_one(name)

def create(explorer: Explorer) -> Explorer:
    """Добавляет новое существо в список и возвращает его."""
    return data.create(explorer)

def modify(explorer: Explorer) -> Explorer:
    return data.modify(explorer)

def replace(explorer: Explorer) -> Explorer:
    return data.modify(explorer)

def delete(name: str)->Explorer:
    return data.delete(name)
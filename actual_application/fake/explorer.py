from model.explorer import Explorer
from error.Web_Exceptions import Missing, Duplicate

_explorers = [
    Explorer(
        name="Marco Polo",
        country="IT",
        description="Venetian merchant and explorer who traveled the Silk Road to China."
    ),
    Explorer(
        name="Christopher Columbus",
        country="SP",
        description="Completed four voyages across the Atlantic Ocean."
    ),
    Explorer(
        name="Ferdinand Magellan",
        country="PT",
        description="Led the first expedition to circumnavigate the globe."
    ),
    Explorer(
        name="James Cook",
        country="GB",
        description="Mapped the Pacific Ocean and discovered Australia."
    ),
    Explorer(
        name="Roald Amundsen",
        country="NW",
        description="First to reach the South Pole in 1911."
    )
]

def get_all()-> list[Explorer]:
    return _explorers

def get_one(name: str) -> Explorer:
    """Возвращает одного исследователя по имени или вызывает исключение, если не найдено."""
    for explorer in _explorers:
        if explorer.name == name:
            return Explorer
    raise Missing(name, 'Explorer')

def create(explorer: Explorer) -> Explorer:
    """Добавляет нового исследователя в список и возвращает его."""
    try:
        get_one(explorer.name)
    except Missing:
        _explorers.append(explorer)
        return explorer
    else:
        raise Duplicate(explorer.name, 'Explorer')


def modify(name: str, explorer: Explorer) -> Explorer:
    deprecated_Explorer = get_one(name)
    deprecated_Explorer.name = explorer.name
    deprecated_Explorer.aka = explorer.aka
    deprecated_Explorer.area = explorer.area
    deprecated_Explorer.country = explorer.country
    deprecated_Explorer.description = explorer.description
    return deprecated_Explorer

def replace(name: str, explorer: Explorer) -> Explorer:
    return modify(name, explorer)

def delete(name: str):
    _explorers.remove(get_one(name))
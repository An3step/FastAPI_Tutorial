from model.explorer import Explorer

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

def get_one(name: str)->Explorer | None:
    for explorer in _explorers:
        if explorer.name == name:
            return explorer
    return None

def create(explorer: Explorer)->Explorer:
    return explorer

def modify(explorer: Explorer)->Explorer:
    return explorer

def replace(explorer: Explorer)->Explorer:
    return explorer

def delete(name: str):
    return None
from model.creature import Creature

_creatures = [
    Creature(
        name="Loch Ness Monster",
        country="SL",
        area="Loch Ness",
        description="A large aquatic creature allegedly inhabiting Loch Ness.",
        aka="Nessie"
    ),
    Creature(
        name="Bigfoot",
        country="US",
        area="Pacific Northwest",
        description="A large, hairy, ape-like creature said to live in forests.",
        aka="Sasquatch"
    ),
    Creature(
        name="Chupacabra",
        country="PR",
        area="Latin America",
        description="A creature said to attack and drink the blood of livestock.",
        aka="Goat Sucker"
    ),
    Creature(
        name="Kraken",
        country="NW",
        area="North Atlantic Ocean",
        description="A giant sea monster capable of sinking ships.",
        aka="The Beast"
    )
]

def get_all() -> list[Creature]:
    """Возвращает всех существ из списка."""
    return _creatures

def get_one(name: str) -> Creature | None:
    """Возвращает одно существо по имени или None, если не найдено."""
    for creature in _creatures:
        if creature.name == name:
            return creature
    return None

def create(creature: Creature) -> Creature:
    """Добавляет новое существо в список и возвращает его."""
    _creatures.append(creature)
    return creature

def modify(creature: Creature) -> Creature:
    return creature

def replace(creature: Creature) -> Creature:
    return creature

def delete(name: str):
    return None
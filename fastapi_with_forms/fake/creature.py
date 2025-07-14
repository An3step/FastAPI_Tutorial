from model.creature import Creature
# from error.Web_Exceptions import Missing, Duplicate

creatures = [
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

# def get_all() -> list[Creature]:
#     """Возвращает всех существ из списка."""
#     return _creatures

# def get_one(name: str) -> Creature:
#     """Возвращает одно существо по имени или None, если не найдено."""
#     for creature in _creatures:
#         if creature.name == name:
#             return creature
#     raise Missing(name, 'Creature')

# def create(creature: Creature) -> Creature:
#     """Добавляет новое существо в список и возвращает его."""
#     try:
#         get_one(creature.name)
#     except Missing:
#         _creatures.append(creature)
#         return get_one(creature.name)
#     else:
#         raise Duplicate(creature.name, 'Creature')


# def modify(name: str, creature: Creature) -> Creature:
#     deprecated_creature = get_one(name)
#     deprecated_creature.name = creature.name
#     deprecated_creature.aka = creature.aka
#     deprecated_creature.area = creature.area
#     deprecated_creature.country = creature.country
#     deprecated_creature.description = creature.description
#     return get_one(creature.name)

# def replace(name: str, creature: Creature) -> Creature:
#     return modify(name, creature)

# def delete(name: str):
#     _creatures.remove(get_one(name))
from pydantic import BaseModel
import datetime

class Creature(BaseModel):
    name: str
    country: str
    # aka: str
    description: str
    # date_time: datetime.datetime = datetime.datetime.now()

# _creatures = [
#     Creature(
#         name='Yeti',
#         country='Nepal',
#         aka='Abominable Snowman',
#         description='A mythical ape-like creature said to inhabit the Himalayan mountains.'
#     ),
#     Creature(
#         name='Loch Ness Monster',
#         country='Scotland',
#         aka='Nessie',
#         description='A creature said to inhabit Loch Ness, often described as large and long-necked.'
#     ),
#     Creature(
#         name='Chupacabra',
#         country='Puerto Rico',
#         aka='Goat-sucker',
#         description='A legendary creature known for attacking livestock, especially goats.'
#     ),
#     Creature(
#         name='Bigfoot',
#         country='USA',
#         aka='Sasquatch',
#         description='A large, hairy, ape-like creature said to inhabit North American forests.'
#     ),
# ]

# def get_Creatures() -> list[Creature]:
#     return _creatures
from model.creature import Creature
from service import creature as code

sample = Creature(name='Yeti',
                  country='CN',
                  area = 'Himalayas',
                  description='Hirsuite Himalayan',
                  aka='Snowman')

def test_create():
    response = code.create(sample)
    assert response == sample

def test_get_existed():
    response = code.get_one('Yeti')
    assert response == sample

def test_get_missing():
    response = code.get_one("djdjdjdjjd")
    assert response is None
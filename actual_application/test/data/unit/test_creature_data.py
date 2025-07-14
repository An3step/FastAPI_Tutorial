import os
import pytest
from model.creature import Creature
from error.Web_Exceptions import Duplicate, Missing
os.environ['CRYPTID_SQLITE_DB'] = ':memory:'
from data import creature as data

@pytest.fixture
def sample() -> Creature:
    return     Creature(
        name="Yeti",
        country="HM",
        area="MT",
        description="A giant snowy monster capable of sinking people.",
        aka="The Beast"
    )

@pytest.fixture
def creatures()->list[Creature]:
    return data.get_all()

def test_create(sample):
    resp = data.create(sample)
    assert resp == sample

def test_create_duplicate(sample):
    with pytest.raises(Duplicate):
        data.create(sample)

def test_get_one(creatures):
    assert data.get_one(creatures[0].name) == creatures[0]

def test_get_one_missing():
    with pytest.raises(Missing):
        data.get_one('abracadabra')

def test_modify(sample):
    sample.country = 'US'
    resp = data.modify(sample.name, sample)
    assert resp == sample

def test_modify_missing(sample):
    with pytest.raises(Missing):
        data.modify('debicus', sample)

def test_delete(creatures):
    print(data.get_all())
    data.delete(creatures[0].name)

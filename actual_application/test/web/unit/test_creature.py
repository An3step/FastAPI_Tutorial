from fastapi import HTTPException
import pytest
import os
os.environ['CRYPTID_UNIT_TEST'] = 'true'
from model.creature import Creature
from web import creature

@pytest.fixture
def sample() -> Creature:
    return Creature(name='dragon', country='*', area='CT', description='FIRE!!!!', aka='beast')

@pytest.fixture
def fakes()->list[Creature]:
    creature.get_all().clear()
    creature.get_all().extend([
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
])
    return creature.get_all()

def assert_duplicate(exc : HTTPException):
    assert exc.value.status_code == 404
    assert 'already exists' in exc.value.msg

def assert_missing(exc : HTTPException):
    assert exc.value.status_code == 404
    assert 'not found' in exc.value.msg

def test_create(sample):
    assert creature.create(sample) == sample

def test_create_duplicate(fakes):
    with pytest.raises(HTTPException) as exc:
        creature.create(fakes[0])
        assert_duplicate(exc)

def test_get_one(fakes):
    assert creature.get_one(fakes[0].name) == fakes[0]

def test_get_one_missing():
    with pytest.raises(HTTPException) as exc:
        creature.get_one('bobcat')
        assert_missing(exc)

def test_modify(fakes):
    assert creature.modify(fakes[0].name, fakes[0]) == fakes[0]

def test_modify_missing(sample):
    with pytest.raises(HTTPException) as exc:
        creature.modify(sample.name, sample)
        assert_missing(exc)

def test_delete(fakes):
    assert creature.delete(fakes[0].name) is None

def test_delete_missing(sample):
    with pytest.raises(HTTPException) as exc:
        creature.delete('emu')
        assert_missing(exc)


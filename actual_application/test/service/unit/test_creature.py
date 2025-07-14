import os
import pytest
from model.creature import Creature
from error.Web_Exceptions import Missing, Duplicate

os.environ['CRYPTID_UNIT_TEST'] = 'true'
from service import creature as service

@pytest.fixture
def sample() -> Creature:
    return     Creature(
        name="Yeti",
        country="HM",
        area="MT",
        description="A giant snowy monster capable of sinking people.",
        aka="The Beast"
    )

@pytest.fixture(autouse=True)
def creatures_reset():
    service.get_all().clear()
    service.get_all().extend(
    [
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
    )

def test_create(sample):
    resp = service.create(sample)
    assert resp == sample

def test_create_duplicate(sample):
    resp = service.create(sample)
    assert resp == sample
    with pytest.raises(Duplicate):
        resp = service.create(sample)

def test_get_exists(sample):
    resp = service.create(sample)
    assert resp == sample
    resp = service.get_one(sample.name)
    assert resp == sample

def test_get_missing():
    with pytest.raises(Missing):
        service.get_one('boxq')

def test_modify(sample):
    sample.country = 'CA'
    resp = service.modify("Loch Ness Monster", sample)
    assert resp == sample

def test_modify_missing(sample):
    with pytest.raises(Missing):
        service.modify(sample.name, sample)
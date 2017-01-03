from faker import Faker

import pytest

from faker_extras import (
    alien,
    biology,
    binary,
    chemistry,
    human,
)


@pytest.fixture()
def fake():
    _fake = Faker()
    _fake.add_provider(human.HumanProvider)
    _fake.add_provider(alien.AlienProvider)
    _fake.add_provider(binary.BinaryProvider)
    _fake.add_provider(chemistry.ChemistryProvider)
    _fake.add_provider(biology.GeneticProvider)
    return _fake

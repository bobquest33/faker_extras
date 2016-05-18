from faker import Faker

from faker_extras import chemistry

fake = Faker()

fake.add_provider(chemistry.ChemistryProvider)


def test_family():
    assert isinstance(fake.family(), str)


def test_period():
    assert isinstance(fake.period(), str)


def test_symbol():
    assert len(fake.symbol()) < 4
    assert isinstance(fake.symbol(), str)


def test_element():
    assert isinstance(fake.element(), str)


def test_atomic_number():
    assert fake.atomic_number() < 119
    assert isinstance(fake.atomic_number(), int)

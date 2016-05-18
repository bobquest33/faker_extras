from faker import Faker

from faker_extras import human

fake = Faker()

fake.add_provider(human.HumanProvider)


def test_pos_attribute():
    assert isinstance(fake.pos_attribute(), str)


def test_neg_attribute():
    assert isinstance(fake.neg_attribute(), str)


def test_mood():
    assert isinstance(fake.mood(), str)


def test_gender():
    assert isinstance(fake.gender(), str)


def test_religion():
    assert isinstance(fake.religion(), str)


def test_race():
    assert isinstance(fake.race(), str)


def test_eye_color():
    assert isinstance(fake.eye_color(), str)


def test_hair_color():
    assert isinstance(fake.hair_color(), str)


def test_shirt_size():
    assert isinstance(fake.shirt_size(), str)


def test_hair_style():
    assert isinstance(fake.hair_style(), str)

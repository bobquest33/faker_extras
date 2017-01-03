
def test_family(fake):
    assert isinstance(fake.family(), str)


def test_period(fake):
    assert isinstance(fake.period(), str)


def test_symbol(fake):
    assert len(fake.symbol()) < 4
    assert isinstance(fake.symbol(), str)


def test_element(fake):
    assert isinstance(fake.element(), str)


def test_atomic_number(fake):
    assert fake.atomic_number() < 119
    assert isinstance(fake.atomic_number(), int)

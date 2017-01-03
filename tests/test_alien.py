
def test_species(fake):
    assert isinstance(fake.alien_species(), str)


def test_name(fake):
    assert isinstance(fake.alien_name(), str)

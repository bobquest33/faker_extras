from faker import Faker

from faker_extras import biology

fake = Faker()

fake.add_provider(biology.GeneticProvider)


def test_amino_acid_group():
    assert isinstance(fake.amino_acid_group(), str)


def test_amino_acid_symbol():
    assert isinstance(fake.amino_acid(symbol=True), str)


def test_amino_acid():
    assert isinstance(fake.amino_acid(), str)


def test_rna():
    assert isinstance(fake.rna(), str)


def test_dna():
    assert isinstance(fake.dna(), str)

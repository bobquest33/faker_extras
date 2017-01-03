
def test_amino_acid_group(fake):
    assert isinstance(fake.amino_acid_group(), str)


def test_amino_acid_symbol(fake):
    assert isinstance(fake.amino_acid(symbol=True), str)


def test_amino_acid(fake):
    assert isinstance(fake.amino_acid(), str)


def test_rna(fake):
    assert isinstance(fake.rna(), str)


def test_dna(fake):
    assert isinstance(fake.dna(), str)

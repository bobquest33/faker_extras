
def test_binary_byte_str_code(fake):
    assert isinstance(fake.binary_byte_str(code=True), str)


def test_decimal_byte_str_code(fake):
    assert isinstance(fake.decimal_byte_str(code=True), str)


def test_binary_byte_str(fake):
    assert isinstance(fake.binary_byte_str(), str)


def test_decimal_byte_str(fake):
    assert isinstance(fake.decimal_byte_str(), str)


def test_nibble(fake):
    assert len(fake.nibble()) == 4
    assert isinstance(fake.nibble(), str)


def test_octet(fake):
    assert len(fake.octet()) == 8
    assert isinstance(fake.octet(), str)


def test_byte(fake):
    assert len(fake.byte()) == 8
    assert isinstance(fake.byte(), str)


def test_word(fake):
    assert len(fake.word()) == 16
    assert isinstance(fake.word(), str)

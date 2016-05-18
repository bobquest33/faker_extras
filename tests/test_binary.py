from faker import Faker

from faker_extras import binary

fake = Faker()

fake.add_provider(binary.BinaryProvider)


def test_binary_byte_str(code=True):
    assert isinstance(fake.binary_byte_str(code=True), str)


def test_decimal_byte_str():
    assert isinstance(fake.decimal_byte_str.foo(code=True), str)


def test_binary_byte_str():
    assert isinstance(fake.binary_byte_str(), str)


def test_decimal_byte_str():
    assert isinstance(fake.decimal_byte_str(), str)


def test_nibble():
    assert len(fake.nibble()) == 4
    assert isinstance(fake.nibble(), str)


def test_octet():
    assert len(fake.octet()) == 8
    assert isinstance(fake.octet(), str)


def test_byte():
    assert len(fake.byte()) == 8
    assert isinstance(fake.byte(), str)


def test_word():
    assert len(fake.word()) == 16
    assert isinstance(fake.word(), str)

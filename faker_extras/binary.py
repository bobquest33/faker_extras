"""Faker data providers for binary data."""

from faker import Faker
from faker.providers import BaseProvider

import utils


class BinaryProvider(BaseProvider):
    """Provide binary data."""

    def nibble(self):
        """Return a nibble.

        >>> nibble()
        >>> 0101
        """
        return utils._choice_str([0, 1], 4)

    def octet(self):
        """Return an octet.

        >>> octet()
        >>> 01011010
        """
        return utils._choice_str([0, 1], 8)

    def byte(self):
        """Return a byte.

        >>> octet()
        >>> 01011010
        """
        return utils._choice_str([0, 1], 8)

    def word(self):
        """Return a 'word'.

        >>> word()
        >>> 0010101111101011
        """
        return utils._choice_str([0, 1], 16)


if __name__ == '__main__':
    fake = Faker()
    fake.add_provider(BinaryProvider)
    print(fake.nibble())
    print(fake.octet())
    print(fake.byte())
    print(fake.word())

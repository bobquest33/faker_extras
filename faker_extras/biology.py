"""Faker data providers for biological data."""

from faker import Faker
from faker.providers import BaseProvider

import utils


class GeneticProvider(BaseProvider):
    """Genomic data provider."""

    def rna(self):
        """Return some RNA sequence.

        >>> rna()
        >>> AAACUAGCUG
        """
        return utils._choice_str(['U', 'C', 'G', 'A'], 10)

    def dna(self):
        """Return some DNA sequence.

        >>> dna()
        >>> CTATAGAGCT
        """
        return utils._choice_str(['T', 'C', 'G', 'A'], 10)


if __name__ == '__main__':
    fake = Faker()
    fake.add_provider(GeneticProvider)
    print(fake.rna())
    print(fake.dna())

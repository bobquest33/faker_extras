[![Build Status](https://travis-ci.org/christabor/faker_extras.svg?branch=master)](https://travis-ci.org/christabor/faker_extras)

# faker_extras
Extra data providers for the [Python Faker library.](https://github.com/joke2k/faker/)

## Current providers

### Binary
Binary data, octets, bits, and bytes.

### Chemistry
Chemistry related data, like elements, atomic numbers, etc...

### Human
An extended version of the person set from faker. Things like, race, religion, gender, etc...

### Biology
Biological encodings, such as RNA and DNA.

## Usage
Install using pip or setuptools: `python setup.py install`

Add the appropriate provider:

```python
from faker import Faker
from faker_extras.biology import GeneticProvider

fake = Faker()
fake.add_provider(GeneticProvider)

fake.dna()
```

## Tests

Run ```nosetests```

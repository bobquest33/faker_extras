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

```python
from faker_extras.biology import GeneticProvider

gen = GeneticProvider()
gen.dna()
```

## Tests

Run ```nosetests```

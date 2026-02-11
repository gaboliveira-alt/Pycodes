
from collections import namedtuple
from typing import NamedTuple

class Card(NamedTuple):
    value: str = 'VALUE'
    naipe: str = 'NAIPE'

Card1 = namedtuple('card', ['value', 'naipe'], defaults=['VALUE', 'NAIPE']) 

as_swords = Card1('A')
print(as_swords._asdict())
print(as_swords)
print(as_swords.value)
print(as_swords.naipe)
print(as_swords[0])
print(as_swords[1])

print()
print(as_swords._fields)
print(as_swords._field_defaults)

for card in as_swords:
    print(card)
# from random import randint
from Pokedex import print_pokemon

# print(randint(1, 10000))



Pokemon = [
    { 'name': 'bulbasaur',
      'types': ['grass', 'poison'],
      'gender': 'f',
      'evolves_to': 'TBD',
      'number': '001',
      'blurb': "bulb lookin dude ",
      'height': 7,
      'weight': 69,
      'evolution_level': 16,
      'eveolves_to': ["ivysaur"]
    },
    { 'name': 'eevee',
      'types': ['grass', 'poison'],
      'gender': 'f',
      'evolves_to': 'TBD',
      'number': '070',
      'blurb': "fox lookin dude ",
      'height': 7,
      'weight': 69,
      'evolution_level': 16,
      'eveolves_to': ["ivysaur"]
    }
]    

print_pokemon(0)
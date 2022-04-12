# Pokedex

# LIST of Pokemon (as dicts)                          DATA
                                                    # Name (String)
                                                    # Type [(String)]
                                                    # Gender (String)
                                                    # Number (String)
                                                    # Evolved_to
                                                    # Blurb (string)
                                                    # Height
                                                    # Weight
                                                    # Level_Evolves

def print_pokemon(poke):
    print(f'''
    Pokemon {poke['number']}: {poke['name']}
    Type/s: {poke['types']}
    Blurb {poke['blurb']}
    ''')


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

print_pokemon(poke[1])
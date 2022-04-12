# Pokedex

# LIST OF PLAYERS                         DATA
                                                    # Name (String)
                                                    # Weight [(String)]
                                                    # Height (String)
                                                    # Number (String)
                                                    # Positions
                                                    # Year Drafted (int)
def print_players(player):
    print(f"""
    Name:  {player['Name']}:
    Weight: {player['Weight']}
    Height: {player['Height']}
    Number: {player['Number']}
    """)

Players = [
    {
        "Name": "Dak Prescott",
        "Weight": "226lbs",
        "Height": "6' 02",
        "Number": 4,
        "Position": "QB",
        "Year Drafted": 2016,
    },
    {
        "Name": "Ezekiel Elliott",
        "Weight": "225",
        "Height": "6' 00",
        "Number": 21,
        "Position": "RB",
        "Year Drafted": 2016,
    },
    {
        "Name": "Tony Pollard",
        "Weight": "210",
        "Height": "6' 00",
        "Number": 20,
        "Position": "WR",
        "Year Drafted": 2019,
    },
    {
        "Name": "Ceedee Lamb",
        "Weight": "198",
        "Height": "6' 02",
        "Number": 88,
        "Position": "WR",
        "Year Drafted": 2020,
    },
    {
        "Name": "Dalton Schultz",
        "Weight": "244lbs",
        "Height": "6' 05",
        "Number": 86,
        "Position": "WR",
        "Year Drafted": 2018,
        
    }


]

print_players(Players[0])
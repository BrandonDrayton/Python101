noun = input("Enter a noun: ")
pt_verb = input("Enter a present-tense verb: ")
name = input("Enter a name ")

def madlib(noun, pt_verb, name):
    print(f""" In a galaxy far far away, there was {name} who {pt_verb} around the {noun}. 
    Everytime {name} {pt_verb} away, the {noun} would fall down""")

madlib(noun, pt_verb, name)
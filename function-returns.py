from cgi import print_directory


def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def div(a, b):
    return a / b

def mul(a,b):
    return a * b

guests = int(input( "How many guests? "))
pancakes = int(input( "How many pancakes? "))    

def calc(guests, pancakes):
    total_pancakes = mul(guests, pancakes) * 1.12
    print(total_pancakes)

calc(guests, pancakes)

temperature_f = int(input( "What is the temperature in fahrenheit? "))
temperature_c = int(input( "What is the temperature in celsius ?"))

def fahrenheitToCelsius(temperature_f):
    celsius = div(mul(sub(temperature_f, 32), 5), 9)
    print(celsius)

fahrenheitToCelsius(temperature_f)   

def celsiusToFahrenheit(temperature_c):
    fahrenheit = add( mul(temperature_c, 1.8), 32)
    print(fahrenheit)

celsiusToFahrenheit(temperature_c)
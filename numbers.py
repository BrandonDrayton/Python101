# name = "Brandon"
# age = 4 # integer
# weight = 24 # float

# print(3+3) = 6 python recognizes both numbers and adds them (Does not just print numbers as is)
# print(6 +6.0) =6.0
# print(10 % 3) gives me the odd or even so in this case the remainder is 9 so 1 is the output


# Assignment operator
# num = 10 
# addition assignment operator
# num += 45
# print(num)

# name = "Brandon"
# age = 4.1 #float
# print("Nelson is " + age) # Type Error
# print("Nelson is " + str(age)) # Nelson is 4.1

# Calc Methods

a = 5
b = 2

print( a + b )
print(a - b)
print(a * b)
print(a / b)

# Pancake calculator

def pancake_calc(guests, pancakes):
    exact_pancakes = guests * pancakes
    inflation_pancakes = exact_pancakes * 1.12
    print(round(inflation_pancakes))

pancake_calc(120, 4)

# Temperature Conversion

def fahrenheitToCelsius(temperature):
    celsius = ((temperature - 32) * 5) / 9
    print(celsius)

fahrenheitToCelsius(145)   

def celsiusToFahrenheit(temperature):
    fahrenheit = temperature * 1.8 + 32
    print(fahrenheit)

celsiusToFahrenheit(340)
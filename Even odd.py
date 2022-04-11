# Write a function that when given a number as an input will return true if the number is odd and false if the number is even.

# Write a script that asks the user for a number. Pass the number to the function and then print a message to the console that informs the user if the number was even or odd

# Example Output:

# Enter a number: 7
# It's Odd!
# Enter a number: 2178932
# It's Even!



number = int(input("Enter a number: "))

def even_odd(number):
    if ((number % 2) == 1) == True:
       print("It is Odd!")
    elif ((number % 2) == 1) == False:
        print("It is Even!")

even_odd(number)
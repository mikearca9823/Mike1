# end="" this will combine the two lines
# print("My name is ", end="")
# print("Monty Python.")
#sep="-" This will put a dash instead of a space between words
# print("My", "name", "is", "Monty", "Python.", sep="-")
#sep="-" puts a dash in between / sep="*" puts * in between
# print("My", "name", "is", sep="-", end="*")
# print("Monty", "Python.", sep="*", end="*\n")

# print("Programming", "Essential", "in", sep="***", end="...")
# print("Python")
# print("string" * 2)
# print('i am a string')

#In Python strings the backslash (\) is a special character which announces that the next character has a different meaning, e.g., \n (the newline character) starts a new output line.
# h-e-l-l-o
# print("h", "e", "l", "l", "o", sep="-", end=" bitches")
#exponants 3 x 10 to the 8th power
# print(32e8)

#coding floats
# 6.62607 x 10 38th power
# 1e-24
# print(0.000000000000000000000001)

#I like "Monty Python" *Puts quotes within a string
# print("I like \"Monty Python\"")
# If you open a string with a quote, you have to close it with a quote.
# If you start a string with an apostrophe, you have to end it with an apostrophe.
# print('I like "Monty Python"')

#I'm Monty Python.
# print("I'm Monty Python")
# print('I\'m Monty Python.')

# Boolean True or False
# print(True > False)
# print(True < False)

# print("\I'm\"\n\"\"learning\"\n\"\"Python\"\"\"")
# Exponents 2 ** 2 2 to the 2nd power
# 2 ** 8 = 256
# print((5 * ((25 % 13) + 100) / (2 * 13)) // 2)
# print((2 % -4), (2 ** 3 ** 2))

# Variables
# var = 1
# account_balance = 1000.0
# client_name = 'John Doe'
# print(var, account_balance, client_name)
# print(var)

# john = 3
# mary = 5
# adam = 6

# print(john, mary, adam, sep=',')

# total_apples = john + mary + adam
# print(total_apples)

# kilometers = 12.25
# miles = 7.38

# miles_to_kilometers = miles * 1.61
# kilometers_to_miles = kilometers / 1.61

# print(miles, "miles is", round(miles_to_kilometers, 2), "kilometers")
# print(kilometers, "kilometers is", round(kilometers_to_miles, 2), "miles")


# anything = float(input("Enter a number: "))
# something = anything ** 2.0
# print(anything, "to the power of 2 is", something)

# Finding length of hypotenuse
# leg_a = float(input("Input first leg length: "))
# leg_b = float(input("Input second leg length: "))
# hypo = (leg_a**2 + leg_b**2) ** .5
# print("Hypotenuse length is", hypo)

# leg_a = float(input("Input first leg length: "))
# leg_b = float(input("Input second leg length: "))
# print("Hypotenuse length is", (leg_a**2 + leg_b**2) ** .5)

# asking for first name and last name as input
# fnam = input("May I have your first name, please? ")
# lnam = input("May I have your last name, please? ")
# print("Thank you.")
# print("\nYour name is " + fnam + " " + lnam + ".")

# string * number
# number * string 
#jamesjamesjames
# print("james" * 3)
# print(3 * "an")

# A number less than or equal to zero produces an empty string
# draw a rectangle
# print("+" + 10 * "-" + "+")
# print(("|" + " " * 10 + "|\n") * 5, end="")
# print("+" + 10 * "-" + "+")

# Right angle triangle again
# leg_a = float(input("Input first leg length: ")) 
# leg_b = float(input("Input second leg length: "))
# print("Hypotenuse length is " + str((leg_a**2 + leg_b**2) ** .5))

# 2.6.9 Lab 
# input a float value for variable 'a' here
# a = float(input("Enter first value: "))
# # input a float value for variable 'b' here
# b = float(input("Enter first value: "))
# # output the result of addition here
# print("Addition:", a + b)
# # output the result of subtraction here
# print("Subtraction:", a - b)
# # output the result of multiplication here
# print("Multiplication:", a * b)
# # output the result of division here
# print("divison:", a / b)
# print("|nThat's all, folks!")

# hour = int(input("Starting time (hours): "))
# mins = int(input("Starting time (minutes): "))
# dura = int(input("Event duration (minutes): "))
# # Write your code here
# # find a total of all minutes
# mins = mins + dura
# # find a number of hours hidden in minutes and update the hour
# hour = hour = mins // 60
# # correct minutes to fall in the (0..59) range
# mins = mins % 60
# # correct hours to fall in the (0..23) range
# hour = hour % 24
# print(hour, ":", mins, sep=' ')

# name = input("Enter your name: ")
# print("Hello, " + name + ". Nice to meet you!")
# print("\nPress Enter to end the program.")
# input()
# print("THE END.")

# num_1 = input("Enter the first number: ") # Enter 12
# num_2 = input("Enter the second number: ") # Enter 21
# print(num_1 + num_2) # the program retuns 1221

# my_input = input("Enter something: ") # Example input: hello
# print(my_input * 3) # Expected output: hellohellohello

# x = input("Enter a number: ") # user enters 2
# print(type(x)) # prints <class 'str'>

# x = int(input(11))
# y = int(input(4))
# x = x % y
# x = x % y 
# y = y % x
# print(y)

# y = 2 + 3 * 5.
# print(y)

# x = 1 / 2 + 3 // 3 + 4 ** 2
# print(x)

x = input(3)
y = int(input(6))
print(x * y)
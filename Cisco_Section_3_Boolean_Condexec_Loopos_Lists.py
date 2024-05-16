# print(2 == 2) # Output is true
#Operators
# count black and white sheep separately as long as there are exactly twice as many black sheep as white ones.
# black_sheep = 2
# white_sheep = 1
# black_sheep == 2 * white_sheep
# black_sheep == (2 * white_sheep)

# var = 0 # Assigning 0 to var
# print(var == 0)
# var = 1 # Assigning 1 to var
# print(var == 0)
#output is True on first line, then false on 2nd

#The != (not equal to) operator compares the values of two operands
# if they are equal, the result of the comparison is False. If they are not equal, the result of the comparison is True.
# var = 0 # Assigning 0 to var
# print(var != 0) # False
# var = 1 # Assigning 1 to var
# print(var != 0) # True

# Using one of the comparison operators in Python, write a simple two-line program that takes the parameter n as input, 
# which is an integer, and prints False if n is less than 100, and True if n is greater than or equal to 100.
# n = int(input("Enter a number: "))
# print(n >= 100)

# Conditions and conditional execution
# if tre_or_not:
    # do_this_if_true
# if the_weather_is_good:
#     go_for_a_walk()
# have_lunch 

# if true_or_false_condition:
#     perform_if_condition_true
# else:
#     perform_if_condition_false

# if the_weather_is_good:
#     go_for_a_walk()
# else:
#     go_to_a_theater()
# have_lunch()

# if the_weather_is_good:
#     go_for_a_walk()
#     have_fun()
# else:
#     go_to_a_theater()
#     enjoy_the_movie()
# have_lunch()

# if the_weather_is_good:
#     if nice_restaurant_is_found:
#         have_lunch()
#     else:
#         eat_a_sandwich()
# else:
#     if tickets_are_available:
#         go_to_the_theater()
#     else:
#         go_shopping()

# elif is used to check more than just one condition, and to stop when the first statement which is true is found.
# if the_weather_is_good:
#     go_for_a_walk()
# elif tickets_are_available:
#     go_to_the_theater()
# elif table_is_available:
#     go_for_lunch()
# else:
#     play_chess_at_home()

# Read two numbers
# number1 = int(input("Enter the first number: "))
# number2 = int(input("Enter the second number: "))
# # Choose the larger number
# if number1 > number2:
#     larger_number = number1
# else:
#     larger_number = number2
# # Print the result
# print("The larger number is:", larger_number)

#Example 2
# Read two numbers
# number1 = int(input("Enter the first number: "))
# number2 = int(input("Enter the second number: "))
# # Choose the larger number
# if number1 > number2: larger_number= number1
# else: larger_number = number2
# # Print the results
# print("The larger number is:", larger_number)

#Example 3
# Read three numbers
# number1 = int(input("Enter the first number: "))
# number2 = int(input("Enter the second number: "))
# number3 = int(input("Enter the third number: "))
# # We temporarily assume that the first number is largest
# # We will verigy this soon.
# largest_number = number1
# # We check if the 2nd number is larger than the current largest_number
# # and update the largest_number if needed.
# if number2 > largest_number:
#     largest_number = number2
# # We check if the 3rd number is larger than the current largest_number
# # and update the largest_number if needed.
# if number3 > largest_number:
#     largest_number = number3
# # Print the result
# print("The largest number is:", largest_number)

# PSEUDOCODE AND INTRO TO LOOPS
# largest_number = 999999999
# number = int(input())
# if number == 1:
#     print(largest_number)
#     exit()
# if number > largest_number:
#     largest_number = number
# no output fucked up

# Read three numbers. MAX
# number1 = int(input("Enter the first number: "))
# number2 = int(input("Enter the second number: "))
# number3 = int(input("Enter the third number: "))
# largest_number = max(number1, number2, number3)
# print("The largest number is:", largest_number)

# name = input("Enter flower name: ")
# if name == "Spathiphyllum":
#     print("Yes - Spathiphyllum is the best plant ever!")
# elif name == "spathiphyllum":
#     print("No, I want a big Spathiphyllum!")
# else:
#     print("Spathiphyllum! Not", name + "!")

# income = float(input("Enter the annual income: "))
# if income < 85528:
#     tax = income * 0.18 - 556.02
# tax = round(tax, 0)
# print("The tax is:", tax, "thalers")

#Essentials of the if-elif-else statement
#Common Year or Leap Year
# year= int(input("Enter a year: "))
# if year < 1582:
#     print("Not within the Gregorian calendar period")
# else:
#     if year % 4 !=0:
#         print("Common year")
#     elif year % 100 !=0:
#         print("Leap year")
#     elif year % 400 !=0:
#         print("Common Year")
#     else:
#         print("Leap year")

# x = 10
# if x == 10:
#     print("x is equal to 10")

x = 10
if x > 5: #condition one
    print("x is greater than 5")
if x < 10: # condition two
    print("x is < 10")
if x == 10:
    print("x is equal to 10")
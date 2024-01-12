#  DATA TYPES
# String 
# subscripting is the method of disceting a string to get a particular letter.
print("hello"[4])
# Integr
print(123 + 345)
# you can separate large numbers with underscores
print(123_456_678)
# Float 
# this represents a decimal number eg. 345.57
# Boolean
# true or false

# FUNCTIONS
number = len(input("what is your name? "))
new_number = str(number)
print("you have " + new_number + " characters in your name")
# the line of code above produces an error, because you can only 
# concatenate strings. to resolve this use the str() function

print (70 + float("100.5"))

# Exercise one
# Write a program that adds the digits in a 
# 2 digit number. e.g. if the input was 35, 
# then the output should be 3 + 5 = 8
# Warning. Do not change the code on line 1.
# Your program should work for different inputs. e.g. any two-digit number.
# The last line of your program should print the result.
two_digit_number = input("input a two digit number")
first = int(two_digit_number[0])
second = int(two_digit_number[1])
result = first + second
print(result)

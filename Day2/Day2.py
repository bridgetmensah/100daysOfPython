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

# the round function is used to round up numbers to whole
# point or specific number of places 
print(round(8/3 , 2))
# the // is used to directly convert a division to integer

final = 4 // 2 
print(final)
final //= 2
print(final)

# F- String in python
score = 12
height = 1.8
isWinnig = True
print(f"your score is {score}, your height is {height}")


# Create a program using maths and
# f-Strings that tells
# us how many weeks we have left, 
# if we live until 90 years old.
# It will take your current age 
# as the input and output
# a message with our time left in this format:
# You have x weeks left
# Where x is replaced with the actual
# calculated number of weeks the 
# input age has left until age 90.

age = input("how ols are you? ")
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
totalweeks = 4680
age_in_weeks = int(age) * 52
age_left = totalweeks - int(age_in_weeks)
print(f"You have {age_left} weeks left.")

# LOVE CALCULATOR
print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
full_name = name1 + name2
lower_name = full_name.lower()

t = lower_name.count("t")
r = lower_name.count("r")
u = lower_name.count("u")
e = lower_name.count("e")

first_digit = t + r + u + e

l = lower_name.count("l")
o = lower_name.count("o")
v = lower_name.count("v")
e = lower_name.count("e")

second_digit = l + o + v + e

love_score = int(str(first_digit) + str(second_digit))

if (love_score < 10) or (love_score > 90):  
  print(f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score >=40 and love_score <= 50:
  print(f"Your score is {love_score}, you are alright together.")
else:
  print(f"Your score is {love_score}.")
  

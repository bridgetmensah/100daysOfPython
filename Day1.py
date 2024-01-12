# PRINT FUNCTION
print("Hello world")
# exercise one on Auditorium
print('Day 1 - Python Print Function')
print('The function is declared like this:')
print("print('what to print')")
# creating a new line using "\n"
print("hey there!\nYou good?")
# string concatenation
print("Hi" + " " + "Bridget")
# exercise two
print("Day 1 - String Manipulation")
print('String Concatenation is done with the "+" sign.')
print('e.g. print("Hello " + "world")')
print("New lines can be created with a backslash and n.")

# INPUT FUNCTION
name = input("what is your first name? ")
# note that the len() function is used to tell the size of a string
print(len(name))

print("hello " + input("what is your last name?"))

num1 = int(input("first number"))
num2= int(input("second number"))
print(num1*num2)

# VARIABLES
# Note that in the above lines of codes, name, num1 etc are varaibles.
# There are two variables, a and b from input
a = '29'
b = '41'
# 🚨 Don't change the code above ☝️
####################################
# Write your code below this line to switch a and b  👇
c = a
a = b
b = c
# 🚨 Don't change the code below 👇
print("a: " + a)
print("b: " + b)
# output: 41
#         29


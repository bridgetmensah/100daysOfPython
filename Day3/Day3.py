# IF ELSE STATEMENTS
condition1 = True
if condition1:
    print("condition 1")
else:
    print("not condtion 1")
    
# NESTED IF ELSE 
if condition1:
    print("condition 1")
    baby_condition = input("True or false? ")
    if baby_condition:
        print("this is baby condition")
    else:
        print("not baby condition")
else:
    print("not condtion 1")

# note the if lese between the original if else statement we wrote. 
# the econd if else is nested.
# IF , ELIF, ELSE 
if condition1:
    print("condition 1")
    baby_condition = input("True or false? ")
    child_condition = input("child or no child")
    if baby_condition:
        print("this is baby condition")
    elif child_condition:
        print("not baby condition")
    else:
        print("no condition")
else:
    print("not condtion 1")

# elif is known as else if . it is used when there are several 
# other comparisons to be made 

# exercise 
# Enter your height in meters e.g., 1.55
height = float(input("input height"))
# Enter your weight in kilograms e.g., 72
weight = int(input("input weight"))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bmi = (weight/(height **2))
BMI = round(bmi, 2)
if BMI < 18.5:
  print(f"Your BMI is {BMI}, you are underweight.")
elif BMI >=18.5 and BMI < 25:
  print(f"Your BMI is {BMI}, you have a normal weight.")
elif BMI >=25 and BMI <30:
  print(f"Your BMI is {BMI}, you are slightly overweight.")
elif BMI >=30 and BMI <35:
  print(f"Your BMI is {BMI}, you are obese.")
else:
  print(f"Your BMI is {BMI}, you are clinically obese.")
  
# exercise 3
# Which year do you want to check?
year = int(input("input a year "))
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("Leap year")
    else:
      print("Not leap year")
  else:
    print("Leap year")
else:
  print("Not leap year")
  
#   PIZZA QUESTION
print("Thank you for choosing Python Pizza Deliveries!")
size = input() # What size pizza do you want? S, M, or L
add_pepperoni = input() # Do you want pepperoni? Y or N
extra_cheese = input() # Do you want extra cheese? Y or N
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
small = 15
medium = 20
large = 25
# for small pizza 
if size == 'S':
  if add_pepperoni == 'Y':
    if extra_cheese == 'Y':
      bill = small + 3
      print(f"Your final bill is: {bill}.")
    else:
      bill = small + 2
      print(f"Your final bill is: {bill}.")
  elif add_pepperoni == 'N':
    if extra_cheese == 'Y':
      bill = small + 1
      print(f"Your final bill is: {bill}.")
    else:
      bill = small 
      print(f"Your final bill is: {bill}.")
  else:
    bill = small 
    print(f"Your final bill is: {bill}.")
# for larger pizza 
elif size == 'L':
  if add_pepperoni == 'Y':
    if extra_cheese == 'Y':
      bill = large + 4
      print(f"Your final bill is: {bill}.")
    else:
      bill = large + 3
      print(f"Your final bill is: {bill}.")
  elif add_pepperoni == 'N':
    if extra_cheese == 'Y':
      bill = large + 1
      print(f"Your final bill is: {bill}.")
    else:
      bill = large 
      print(f"Your final bill is: {bill}.")
  else:
    bill = large 
    print(f"Your final bill is: {bill}.")
    
# for medium pizza 
elif size == 'M':
  if add_pepperoni == 'Y':
    if extra_cheese == 'Y':
      bill = medium + 4
      print(f"Your final bill is: {bill}.")
    else:
      bill = medium + 3
      print(f"Your final bill is: {bill}.")
  elif add_pepperoni == 'N':
    if extra_cheese == 'Y':
      bill = medium + 1
      print(f"Your final bill is: {bill}.")
    else:
      bill = medium 
      print(f"Your final bill is: {bill}.")
  else:
    bill = medium 
    print(f"Your final bill is: {bill}.")
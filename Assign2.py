"""
Write a program that does the following:
Asks the user to enter in 2 numbers that can be float values
Ask the user if one of the numbers is the hypotenuse of a right triangle
Calculates the length of the missing side and rounds it to 1 decimal place.
"""
x = input("Write a number ")
y = input("Write another number ")
x = float(x)
y = float(y)
if x > y:
 h1 = input("was the first number the hypotonuse?")
 h2 = "false"
if x < y:
 h2 = input("was the second number the hypotonuse?")
 h1 = "false"

if h1 == "no":
    print(((x**2)+(y**2))**0.5)
elif h1 == "yes":
    print(((x**2)-(y**2))**0.5)
if h2 == "no":
    print(((x**2)+(y**2))**0.5)
elif h2 == "yes":
    print(((y**2)-(x**2))**0.5)


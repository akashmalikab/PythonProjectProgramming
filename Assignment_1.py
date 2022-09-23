# 1. Write a Python program to print "Hello Python"?
print("Hello Python")

# 2. Write a Python program to do arithmetical operations addition and division.?

a=b=5
def addition():
    return a+b

def division():
    return a/b

print(addition())
print(division())


# 3. Write a Python program to find the area of a triangle?
def areaoftriangle():
    base = float(input("Enter base of triangle : "))
    height = float(input("Enter height of triangle : "))
    area = (1/2)*(height*base)
    return f"Area of triangle is {area} "

print(areaoftriangle())

# 4. Write a Python program to swap two variables?
def swaptwovariables(x,y):
    temp = x
    x = y
    y = temp
    return f"Value of x is {x} and Value of y is {y}"

print(swaptwovariables(x=3,y=4))

# 5. Write a Python program to generate a random number?
import random
number = random.random()
print(number)

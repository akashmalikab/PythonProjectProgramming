# 1. Write a Python program to convert kilometers to miles?
def kmTOmiles():
    km = float(input("Pleas enter km here : "))
    miles = (0.62)*km
    return f"We have {miles} miles in {km} kilometers "

print(kmTOmiles())


# 2. Write a Python program to convert Celsius to Fahrenheit?
def celTOfer():
    celcius = float(input("Pleas enter celcius here : "))
    faranhite = (celcius * 1.8) + 32
    return f"We have {faranhite} faranhite in {celcius} celcius "

print(celTOfer())

# 3. Write a Python program to display calendar?
import calendar
print(calendar.calendar(2022)) #we can pass specific month for a specific year ==> print(calendar.month(yy,mm))

# 4. Write a Python program to solve quadratic equation?
import cmath

x = float(input('Enter x: '))
y = float(input('Enter y: '))
z = float(input('Enter z: '))

# calculate the discriminant
disc = (y ** 2) - (4 * x * z)

# find two solutions
sol1 = (-y - cmath.sqrt(disc)) / (2 * x)
sol2 = (-y + cmath.sqrt(disc)) / (2 * x)
print('The solution are {0} and {1}'.format(sol1, sol2))

# 5. Write a Python program to swap two variables without temp variable?
def swapnumbers():
    a = input("Enter value of a : ")
    b = input("Enter value of b : ")
    a,b = b,a
    return f"a value after swapping is {a} and value of b is {b}"

print(swapnumbers())
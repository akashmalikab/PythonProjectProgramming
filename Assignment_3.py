# 1. Write a Python Program to Check if a Number is Positive, Negative or Zero?
def numbercheck():
    a = int(input("Please enter a number : "))
    if a == 0:
        return "Number is ZERO"
    elif a > 0 :
        return "Number is positive"
    else:
        return "Number is negative"
print(numbercheck())

# 2. Write a Python Program to Check if a Number is Odd or Even?
def oddeven():
    a = int(input("Please enter a number : "))
    if a % 2 == 0:
        return "Number is EVEN"
    else:
        return "Number is odd"
print(oddeven())

# 3. Write a Python Program to Check Leap Year?

def leapyear():
    year = int(input("Enter year : "))
    if (year % 400 == 0) and (year % 100 == 0):
        return "{0} is a leap year".format(year)
    elif (year % 4 ==0) and (year % 100 != 0):
        return "{0} is a leap year".format(year)
    else:
        return  "{0} is not a leap year".format(year)
print(leapyear())

# 4. Write a Python Program to Check Prime Number?
def primenumber():
    a = int(input("Please enter a number greater than 1 : "))
    for i in range(2, int(a / 2) + 1):
        if (a % i) == 0:
            return f"{a}is not a prime number"
            break
        else:
            return f"{a}is a prime number"
    else:
        return  f"{a}is not a prime number"
print(primenumber())

# 5. Write a Python Program to Print all Prime Numbers in an Interval of 1-10000?
def printprimenumber():
    for number in range(1,1000+1):
        if number > 1:
            for i in range(2, number):
                if (number % i) == 0:
                    break
            else:
                print(number)
        else:
            print(1)
print(printprimenumber())
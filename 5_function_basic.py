# function defination in python 
from asyncio.windows_events import NULL
from ctypes import sizeof


def sum (a,b):
    return (a+b)
# indented part is inside the function
# function stops as soon as it encounters return statement
print(sum(5,6))
# function definition is important before using function
# recurssion
# recurssion is calling a function when running the same function
def fact(a):
    if a<=0:
        return (1)
    else:
        return(a*fact(a-1))

print(fact(4))

# prime upto n


def isprime(num):
    li=[]
    for i in range (1,num+1):
        if num%i ==0:
            li=li+[i]
    if len(li)==2:
        return True
    else:
        return False


def primeupto(num):
    li=[]
    for i in range (1,num+1):
        if isprime(i):
            li=li + [i]
    return li

print(primeupto(10))
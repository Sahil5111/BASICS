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

#isprime checks a given number whether given number is prime or not
def isprime(num):
    li=[]
    for i in range (1,num+1):
        if num%i ==0:#here funtion is checking divisiblity by i which is between 1 and num
            li=li+[i]
    if len(li)==2:
        return True
    else:
        return False

# runs a loop to check numbers from 1 to num
def primeupto(num):
    li=[]
    for i in range (1,num+1):
        if isprime(i):#calling is prime
            li=li + [i]
    return li

print(primeupto(10))
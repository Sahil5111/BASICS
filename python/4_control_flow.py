# if else statements in python
a=11
if a==0 :
    print("programming is easy")
else :
    print("programming is not easy")
# only indented part falls in the conditional, in python empty sequence is treated as false and any value other than 0 is true 


# if else if ladder in python
if a>10:
    print("number is greater than 10")
elif 5>a>10:
    print("number is between 5 and 10")
else :
    print("number is smaller than 5")


# loops in python 
for i in range(0,6):#as expected this range ends one before upper limit 
    print(i)
# and loop runs for every integral value between limits of range
# while loop in pyrhon 
while a<=20 :
    print(a)
    a=a+1

# naive algorithm to check pos in given a list 
# it returns len(a) if element is not found  
def findpos (a,b):
    i=0
    for x in a:
        if x==b:
            break
        i=i+1
    return i

list =[1,3,5,7]

a=findpos(list,10)
print(a)


# smarter function to do the same task
#  else statement for for loop
def smartpos(a,b):
    for i in range(len(a)):
        if b==a[i]:
            pos=i
            break
    else :              #this statement runs if there is no break
        pos =-1 
    return pos 

a=[1,3,5,7]
print(smartpos(a,3))
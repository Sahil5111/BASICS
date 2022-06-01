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

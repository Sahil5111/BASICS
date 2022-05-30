str="string's"
str2='''I say "python is simple"
new line can be added this way as well'''
print(str2) 
# slicing a string
print(str2[:10])#slice is between 0 to 9
print(str[1:7])#slice is between 1 to 6
# we can access last char in python using negative numbers
print(str[-1])
# strings are immutable in python slice is used to change a string
str=str[0:6]+" "
print(str)
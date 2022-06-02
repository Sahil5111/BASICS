# function defination in python 
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
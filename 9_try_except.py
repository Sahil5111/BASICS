# here python tries a certain block of code and runs except block if there is an error

try :
    a=int(input('enter an integer : '))
    print("your input is ",a)
except:
    print("input is not an integer")
else:
    print("congractulations no errors")
finally:
    print("try except finished")

#else statement can be used below except 
#else will run if except dosent runs 
#finally is a keyword where statement in this block will run irrespective of an error  
# here python tries a certain block of code and runs except block if there is an error

try :
    a=int(input('enter an integer : '))
    print("your input is ",a)
except:
    print("input is not an integer")
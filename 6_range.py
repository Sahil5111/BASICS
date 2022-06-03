# range funtion in detail 
# range(i,j) gives i,i+1,...,j-1
# range(j) gives 0,1,2,...,j-1
# range(i,j,k) gives i,i+k,i+2K,...,i+nk ;n is such that last element is smaller than j
# giving negative k we can travel back in a loop


# in short second number should not be crossed
# python works this way for easy working with string

# example of program at line 2 

for i in range(1,11):
    print(i)


# example of program at line 3

for i in range(11):
    print(i)


# example of program at line 4

for i in range(0,11,2):
    print(i)


# example of program at line 5

for i in range(10,0,-2):
    print(i)


# type conversion in python
# list() is used to convert given things to a list 
# str() is used to convert given things to a string
# int() converts given string to an int

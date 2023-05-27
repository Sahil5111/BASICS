# important functions are at line
# 42 46 50 58 

# we can store all types of values
list=[1,"sahil",True]
print(list)

# we can slice lists as well slicing list gives us list 
print(list[:2])
# values can be accessed using position 
print(list[1])
# list can be nested 
a=['engineering','is boring']
list2=[[list,a],False,'list2']
print(list2)#output is [[[1, 'sahil', True], ['engineering', 'is boring']], False, 'list2']
# list is mutable
list[2]=False
print("\n",list,list2)
# line 13 changes all the places where list was assigned because variable assigned to list points to list 
# example
list =[1,3,5,7]
list2 = list
print(list,list2)
list2[2]=4
print(list,list2)

# list can be assigned using slice operation to avoid above feature
# example 
list2 = list[:]#this way list2 is pointing to list stored at different location so changes in either will not affect other
list[3]=6
print(list,list2)#output [1, 3, 4, 6] [1, 3, 4, 7]
# to avoid above confusion is operator is used 
print(list is list2)#is operator checks whether var are pointing to same location

# list concatenation
list=list + list2
print(list)#output [1, 3, 4, 6, 1, 3, 4, 7]

# using concatenation list points to new list 
# to avoid this append is used
list2=list 
list.append(11)#thus both list varisable are pointing at same list 
# print(list2,list)

# extend function 
list.extend([1,5])#thus both list varisable are pointing at same list and multiple things can be added at same time 
print(list2,list)

# even removing a element can make the list to point to other location to avoid this we use remove
list.remove(5)#removes first occurance of num inside brackets
print(list2,list)

# slice operation 
list[3:]=[5,6,7]#as changes are occuring to pointed location both list variables change
print(list2,list)

# 5 in list is command that returns true or false if 5 is in list list
print(11 in list ) 
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
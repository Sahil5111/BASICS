arr=[1,2,3,4,5,6,7,8,9,10]
# iterative binary search that returns position of the required element
def binarysearch(a,b):
    low=0
    high=len(a)-1
    mid=0
    while low<=high:
        mid=(low+high)//2
        if a[mid]==b:
            return mid 
        elif a[mid]<b:
            low =mid+1
        else :
            high =mid-1
    return -1

# recursive binary search that returns true if element is in the list and returns false if element is not int the list
def binarysearch2(a,b):
    mid=(len(a)-1)//2
    if len(a)==0:
        return False
    if a[mid]==b:
        return True
    elif a[mid]>b:
        return(binarysearch2(a[:mid],b))
    else :
        return(binarysearch2(a[mid+1:],b))


print(binarysearch(arr,8))

print(binarysearch2(arr,11))
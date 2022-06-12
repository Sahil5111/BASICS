arr=[1,2,3,4,5,6,7,8,9,10]

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

print(binarysearch(arr,8))
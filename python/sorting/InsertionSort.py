l=[9,8,7,6,5,4,3,2,1]

def insersort(l):
    for i in range(len(l)):
        temp=i
        while temp>0 and l[temp]<l[temp-1]:
            (l[temp],l[temp-1])=(l[temp-1],l[temp])
            temp=temp-1
    return l

print(insersort(l))
list=[10,9,8,7,6,5,4,3,2,1]

def ss(a):
    for i in range(len(a)):
        temp=i
        for j in range(i,len(a)):
             if a[j]<a[i]:
                temp=j
        (a[i],a[temp])=(a[temp],a[i])
    return a

print(ss(list))
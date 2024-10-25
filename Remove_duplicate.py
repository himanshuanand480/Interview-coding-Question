arr=list(map(int,input("Enter the array: ").split()))
arr1=set(arr)
print(arr1)

#method2:-

def remove(arr2):
    n=len(arr2)
    if n==0 or n==1:
        return arr2
    temp=[0]*n
    pivot=0
    for last in range(0,n-1):
        if arr2[last]!=arr2[last+1]:
            temp[pivot]=arr2[last]
            pivot=pivot+1
    temp[pivot]=arr2[n-1]
    return temp[0:pivot+1]
arr=list(map(int,input("Enter the array: ").split()))
arr2=sorted(arr)
print(remove(arr2))

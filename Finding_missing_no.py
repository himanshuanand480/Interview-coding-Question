"""Find missing number in array"""

a=list(map(int,input("Enter the array number: ").split()))
def find_no(a):
    sum1=sum(a)
    n=a[-1]
    sum2=n*(n+1)//2
    print(abs(sum1-sum2))
find_no(a)
        

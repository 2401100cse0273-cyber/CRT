'''
1) write a python code for factorial of a number.
n=int(input("Enter a number: "))
fact=1
for i in range(1,n+1):
    fact=fact*i 
print(fact)

2) write a python code to check whether a number is armstrong or not.
ex: 153 --> 1,5,3 --> (1**3)+(5**3)+(3**3)=153
n=int(input("Enter a number:"))
temp=n
sum=0
while temp>0:
    digit=temp%10
    sum=sum+(digit**3)
    temp=temp//10
if sum==n:
    print("Armstrong number")
else:
    print("Not an Armstrong number")

3) write a python code to check whether a number is prime or not. 
n=int(input("Enter a number:"))
if n>1:
    for i in range(2,n):
        if n%i==0:
            print("Not a prime number")
            break
    else:
        print("Prime number")

4) print the prime numbers with a range.
n=int(input("Enter a number: "))
for i in range(2,n+1):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print(i) 

5) monotonic of a number
ex: 1,2,3,4,5 --> monotonic 
5,4,3,2,1 --> monotonic
5,4,8,6,2,1 --> not monotonic
10,5,6,25,45 --> not monotonic
arr=list(map(int,input().split()))
inc=True 
dec=True 
for i in range(len(arr)-1):
    if arr[i]>arr[i+1]:
        inc=False 
    if arr[i]<arr[i+1]:
        dec=False
if inc or dec:
    print("Monotonic")
else:
    print("Not monotonic")

6) reverse integer.'''
x=int(input("Enter a number:"))
sign=1
if x<0:
    sign=-1
    x=-x
rev=0
while x>0:
    digit=x%10
    rev=rev*10+digit
    x=x//10
rev=rev*sign
if rev<-2**31 or rev>2**31-1:
    print(0)
else:
    print("Reversed Integer: ",rev)
    
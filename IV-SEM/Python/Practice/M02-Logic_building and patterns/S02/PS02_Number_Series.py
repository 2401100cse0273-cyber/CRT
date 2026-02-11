#Number Series:Sequential order of numbers in a particular pattern
'''
1. Print n natural numbers
n=int(input("Enter a number:"))
for i in range(1,n+1):
    print(i) 

2. Print n even numbers
n=int(input("Enter a number:"))
for i in range(2,n+1,2):
    print(i)

3. print n odd numbers
n=int(input("Enter a number:"))
for i in range(1,n+1,2):
    print(i)

4. print n fibonacci series ==> 0,1,1,2,3,5,8,13,21,34...
n=int(input("Enter a number:"))
a=0
b=1
for i in range(n):
    print(a, end=" ")
    c = a + b
    a = b
    b = c

5. print the multiplication table of any number
n=int(input("Enter a number:"))
for i in range(1,11):
    print(n,"x",i,"=",n*i)

6. print the square of first n natural numbers
n=int(input("Enter a number:"))
for i in range(1,n+1):
    print(i**2) #print(i*i)

7. print the cube of first n natural numbers
n=int(input("Enter a number:"))
for i in range(1,n+1):
    print(i**3) #print(i*i*i)

8. print alternate series ==> 1,-2,3,-4,5,-6,...
n=int(input("Enter a number:"))
for i in range(1,n+1):
    if i%2==0:
        print(-i)
    else:
        print(i)

9. output:- -1,2,-3,4,-5,...
n=int(input("Enter a number:"))
for i in range(1,n+1):
    if i%2==0:
        print(i)
    else:
        print(-i)

10. output:- 1,2,4,7,11,16,22,...
n = int(input("Enter a number: "))
num = 1
diff = 1
for i in range(n):
    print(num, end=" ")
    num = num + diff
    diff = diff + 1

11. output:- 1,2,6,24,120,...
n = int(input("Enter a number:"))
fact = 1
for i in range(1, n + 1):
    fact = fact * i
    print(fact, end=" ")
'''

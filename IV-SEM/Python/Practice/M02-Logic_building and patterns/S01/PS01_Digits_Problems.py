'''
1. Count the number of digits in a number.
2. Find the sum of digits of a number.
3. Reverse a number.
4. Check palindrome number.
5. Check Armstrong number.
6. Count even and odd digits.
7. Find largest digit.
8. Find smallest digit.
9. Count zero digits.
10. Find digital root of a number.
11. Check Spy number.
'''
#1. Count the number of digits in a number.
'''
n = int(input())
temp = n
count = 0
while n > 0:
    count += 1
    n //= 10
print(count)
print(len(str(temp)))
'''
#2. Find the sum of digits of a number.
'''
n = int(input())
s = 0
while n > 0:
    s += (n%10)
    n //= 10
print(s)
'''
#Find digital root of a number.
n = int(input())
while n > 10:
    n = sum(list(map(int,str(n)))) 
print(n)
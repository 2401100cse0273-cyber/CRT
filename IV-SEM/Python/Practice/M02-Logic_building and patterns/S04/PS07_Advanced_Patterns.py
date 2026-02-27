'''
1. Pascal Triangle
n=5
Output:
1
1 1
1 2 1
1 3 3 1
1 4 6 4 1
n = int(input())
for i in range(n):
    num = 1
    for j in range(i+1):
        print(num,end=" ")
        num = num * (i-j) // (j+1)
    print()
'''
'''
2. Butterfly Pattern
n=4
Output:
*      *
**    **
***  ***
********
********
***  ***
**    **
*      *
'''
n = int(input())
for i in range(1,n+1):
    print("*"*i + " "*(2*(n-i)) + "*"*i)
for i in range(n,0,-1):
    print("*"*i + " "*(2*(n-i)) + "*"*i)

'''
3. Hourglass Pattern
n=4
Output:
* * * *
* * *
* *
*
* *
* * *
* * * *

4. Concentric Square
n=3
Output:
3 3 3 3 3
3 2 2 2 3
3 2 1 2 3
3 2 2 2 3
3 3 3 3 3

5. Snake Pattern
n=4
Output:
1 2 3 4
8 7 6 5
9 10 11 12
16 15 14 13

6. Spiral Matrix
n=3
Output:
[1, 2, 3]
[8, 9, 4]
[7, 6, 5]

7. Number Spiral
n=5
Output:
[1, 2, 3, 4, 5]
[16,17,18,19,6]
[15,24,25,20,7]
[14,23,22,21,8]
[13,12,11,10,9]

8. X Pattern Numbers
n=5
Output:
1       1
 2   2
   3
 4   4
5       5

9. Hollow Butterfly
n=4
Output:
*      *
**    **
***  ***
********
***  ***
**    **
*      *
'''
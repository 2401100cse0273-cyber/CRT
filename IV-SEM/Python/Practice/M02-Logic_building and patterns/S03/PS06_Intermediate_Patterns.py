'''Intermediante patterns
1. Pyramid
n = 4
Output:
   *
  * *
 * * *
* * * *

2. Inverted Pyramid
n=4
Output:
* * * *
 * * *
  * *
   *

3. Diamond
n=4
Output:
   *
  * *
 * * *
* * * *
 * * *
  * *
   *
4. Number Pyramid
n=4
Output:
   1
  1 2
 1 2 3
1 2 3 4

5. Palindrome Pattern
n=4
Output:
1
212
32123
4321234

6. Reverse Number Triangle
n=4
Output:
1 2 3 4
1 2 3
1 2
1

7. Binary Triangle
n=4
Output:
1
0 1
1 0 1
0 1 0 1

8. Cross Pattern
n=5
Output:
*       *
  *   *
    *
  *   *
*       *

9. Hollow Diamond
n=4
Output:
   *
  * *
 *   *
*     *
 *   *
  * *
   *

10. Hollow Pyramid
n=4
Output:
   *
  * *
 *   *
*******


li = [1,2,3,4,5]
#output : [2,4,6,8,10]
res = []
for ele in li:
    res.append(ele * 2)
print(res)

print([ele* 2 for ele in li])

li = [1,2,3,4,5]
res = []
for i in li:
    if i % 2 == 0:
        res.append(i)
print(res)

print([i for i in li if i % 2 == 0])
print(tuple(i for i in li if i % 2 == 0))
print({i:i*2 for i in li if i % 2 == 0})


li1 = ['a','b','c']
#"a b c"
res = " "
for ch in li1:
    res = res + ch + " "
print(res)

print(" ".join(li1))
'''

n = int(input())
for i in range(1,n+1):
    print(" "*(n-i)+"* "*i)

print() 

for i in range(n,0,-1):
    print(" "*(n-i)+"* "*i)
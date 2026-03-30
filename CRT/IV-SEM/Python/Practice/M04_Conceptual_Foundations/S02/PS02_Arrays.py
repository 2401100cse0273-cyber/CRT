a = [10,23,45,65,1,2,3]
a.sort()
print(a[::-1])

a = [10,23,45,65,1,2,3]
a.sort()
a.reverse()
print(a)

a = [10,23,45,65,1,2,3]
rev=[]
for i in range(len(a)):
    rev = [i] + rev
print(rev)

a = [10,23,45,65,1,2,3]
b = True
for i in range(len(a)-1):
    if a[i] > a[i+1]:
        b = False
print(b)


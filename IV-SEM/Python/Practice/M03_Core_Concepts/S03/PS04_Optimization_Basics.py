a = [10, 20, 30, 40, 52]
for i in range(len(a)):
    for j in range(len(a)):
        print(a[i] + a[j]) 

a = [10, 20, 30, 40, 52]
for num in a:
    print(num + num) 

'''
why optimization is important:
-->Improve progress speed 
-->Reduces the memory usage
-->Avoid nested loops
'''

#Find then sum of numbers from 1 to n
a = [10, 20, 30, 40, 52]
sum1 = 0
for i in range(len(a)):
    sum1 += a[i]
print(sum1)

a = [10, 20, 30, 40, 52]
print(sum(a))

a = []
for i in range(10):
    a.append(i * i)
print(a)

a = print([i * i for i in range(10)])

#find the maximum element in a list 
a = print([])

'''
print("Hello world!")
print("Hello world!")
print("Hello world!")
print("Hello world!")
print("Hello world!")

counter = 0
while counter < 5:
    print("Hello world!")
    counter += 1

#Count the no.of digits in a number
n = int(input())
counter = 0
while n > 0:
    counter += 1
    n //= 10
print(counter)

#Print Hello world! 5 times using for loop
counter = 0
while counter < 5:
    print("Hello world!")
    counter += 1

for counter in range(0,5,1):
    print("Hello world!")

#input : [1,2,3,4,5] output:[1,4,9,16,25]
li = [1,2,3,4,5]
for i in range(len(li)):
    li[i] = li[i] ** 2
print(li)

li = [1,2,3,4,5]
for i in range(len(li)):
    if li[i] % 2 == 0:
        print(li[i],end=" ")

for ele in li:
    if ele % 2 == 0:
        print(ele,end=" ")

s = input()
count = 0
for ch in s:
    if ch in "aeiouAEIOU":
        count += 1
print(count)
'''
for i in range(1,11):
    if i == 5:
        continue
    print(i,end=" ")
'''
Password retry system (max 3 attempts)
If password is correct show login successful
else ask for password 3 times.
Once attempts exceed show account locked.
'''
'''
Data types:
1. Fundamental DT:
    1. int
    2. float
    3. complex
    4. Boolean
    5. String
2. Collection DT:
    1. List
    2. Tuple
    3. Set
    4. Dictionary
'''
x = 12
y = 12.45
z = 4 + 5j
print(x,type(x))
print(y,type(y))
print(z,type(z))

f1 = 3e2
f2 = 4E3
print(f1,type(f1))
print(f2,type(f2))

c1 = 4 + 5j
c2 = complex(2,-3)
print(c1 + c2)
print(c1 - c2)
print(c1 * c2)
print(c1 / c2)

print(c1.real)
print(c1.imag)

s = "python"
print(s[2])
print(s[::])
print(s[::2])
print(s[::-1])
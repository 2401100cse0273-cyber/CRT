'''
# Find the largest Number(using max()) 
n = [1, 4, 7]
print(max(n))

#check Palindrome(using reversed() & join())
s = "racecar"
if s == ''.join(reversed(s)):
    print("Palindrome")
else:
    print("Not a Palindrome")

#Count Even (Numbers(using filter())
nums = [1, 2, 3, 4]
even_count = len(list(filter(lambda x: x % 2 == 0, nums))) 

#Remove Duplicates (using set())
nums = [1, 2, 2, 4]
uni_nums = set(nums)
print(uni_nums)

#Sum of Digits (using sum())
num = 234
sum = sum(int(digit) for digit in str(num)) 
print(sum)

#Sort Words Alphabetically (using sorted)
words = ["Navi", "pali", "kavya"]
sorted_words = sorted(words, key = str.lower)
print(sorted_words)

#Find Common Elements (using sorted())
list1 = [1, 2, 6]
list2 = [2, 4, 6]
common_elements = sorted(set(list1) & set(list2))
print(common_elements)

#Index with value(using enumerate())
Names = ["Naveena", "Navi", "Naya"]
for index, value in enumerate(Names):
    print(index, value)


#Pair two Lists (using zip())
list1 = [7, 8, 9]
list2 = [1, 2, 3]
paired = list(zip(list1, list2))
print(paired)


#Find Second largest (using sorted())
nums = [1, 9, 15]
sorted_nums = sorted(nums, reverse = True)
print(sorted_nums[1])
'''

# def get_number():
#     return 1        # function runs, returns 1, DIES completely

# print(get_number())  


# def gen_rator():
#     yield 1
#     yield 2
#     yield 3

# sen=gen_rator()
# print(next(sen))
# print(next(sen))
# print(next(sen))
# print(next(sen)) ### here i get error becuase here there is no value like yeild 4 so it gives stopiteration error


### most commonly for loop is used in generator inplace of calling all the time next() beacuse for loop automaticalyy does it

# def count_up(limit):
#     i=1
#     while i<=limit:
#         yield i
#         i+=1
# for num in count_up(6):
#     print(num)

# for loop automatically calls next() each time
# When StopIteration happens → for loop ends cleanly
# You never see the StopIteration error

# Fibonacci Numbers (Common Interview Question)  using generator

# def fibonacii_series():
#     a,b=0,1
#     while True:
#         yield a
#         a,b=b,a+b
# res=fibonacii_series()
# for _ in range(10):
#     print(next(res))

# The for _ in range(10) just says "do this 10 times" — the _ is a common convention meaning "I don't actually need this loop variable's value, I just want to repeat something N times."

## using limit like how i solved last problem
# def fibo_nacii(limit):
#     a,b=0,1
#     while a <= limit:
#         yield a
#         a,b=b,a+b
# for i in fibo_nacii(10):
#     print(i)


# Write a generator that produces squares of numbers:
# def square_num(n):
#     for i in range(1,n+1):
#         yield i**2
# for num in square_num(10):
#     print(num)

#####Berribot practice

##Contains duplicate

# def contains_dup(nums):
#     seen=set()
#     for num in nums:
#         if num in seen:
#             return True
#         seen.add(num)
#     return False

# print(contains_dup([1,2,3,4,1]))
# print(contains_dup([1,2,3,4,]))   

## count the vowels in a string

# def count_vowels(words,left,right):
#     count=0
#     vowels="aeiou"
#     for i in range(left,right+1):
#         if words[i][0] in vowels and words[i][-1] in vowels:
#             count+=1
#     return count
# print(count_vowels(["ari","adf","u"],0,1))

## two sum
## num=[2,7,11,15] target=9 o/p=0,2 i should return the index values 
# def two_sum(nums,target):
#     seen={}
#     for i,num in enumerate(nums):
#         complement=target-num
#         if complement in seen:
#             return [seen[complement],i]
#         seen[num]=i

# print(two_sum([2,7,11,15],9))


## valid anagram 

# def valid_anagram(s,t):
#     count_1={}
#     for letter in s:
#         if letter in count_1:
#             count_1[letter]+=1
#         else:
#             count_1[letter]=1
#     count_2={}
#     for letter in t:
#         if letter in count_2:
#             count_2[letter]+=1
#         else:
#             count_2[letter]=1
#     return count_1 == count_2

# print(valid_anagram("anagram","naagram"))
# print(valid_anagram("anagram","naagran"))
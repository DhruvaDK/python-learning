## to printnumbers from 1 to 10
# for i in range(10):
#     print(i+1)

# Print all even numbers from 1 to 20.
# for i in range(1,20,2):
#     print(i+1)

# Calculate the sum of numbers from 1 to 100./
# sum=0
# for i in range(1,100+1):
#     sum+=i
# print(sum)

##now count how many numbers are there in 1 to 100
# count=0
# for i in range (1,101):
#     count+=1
# print(count)

# Given a list nums = [4, 7, 1, 9, 3], print each number multiplied by 2.
# nums=[4,7,2,9,3]
# a=0
# for num in nums:
#     a=num*2
#     print(a)


# Count how many vowels are in the string "leetcode" using a for loop that goes through each character.
# words="leetcode"
# count=0
# vowels="aeiou"
# for char in words:
#     if char in vowels:
#         count+=1
# print(count)

### while loop

## Print numbers from 10 down to 1.
# i=10
# while i > 0:
#    print(i)
#    i-=1

# Keep doubling a number starting from 1, until it exceeds 100 — print each value.

# i=1
# while i<=100:
#     print(i)
#     i*=2


# Given n = 12345, find the sum of its digits. using for loop and while loop
# n="12345"
# sum=0
# for i in n:
#     sum=sum+int(i)
# print(sum)


## using while loop
# n=12345
# sum=0
# while n>0:
#     digit=n%10
#     sum=sum+digit
#     n=n//10
# print(sum)

####Reverse a number using a while loop (e.g., 1234 → 4321).
# n=1234
# reverse_num=0
# while n >0:
#     digit=n%10
#     reverse_num=reverse_num*10+digit
#     n=n//10
# print(reverse_num)
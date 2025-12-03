add =lambda a,b:a+b
print(add(5,3))

square = lambda x:x*x
print(square(4))
print(square(6))
print(square(8))

is_even = lambda x :x % 2 == 0
print(is_even(10))
print(is_even(2))
print(is_even(5))

items = [(1,3),(4,1),(2,3),(4,2),(5,1),(1,2)]
items.sort(key=lambda x:x[0])
print(items)



nums = [1,2,3,4,5,6,7,8]
evens = list(filter(lambda x:x% 2 == 0,nums))
print(evens)




nums = (1,2,3,4,5,6,7,8)
evens = tuple(filter(lambda x:x% 2 == 0,nums))
print(evens)


data = [(1,'a'),(3,'a'),(2,'b')]
result = sorted(data,key=lambda x:x[0])
print(result)



# Map

# multiply each number by 3
num = [1,2,3,4]
result = list(map(lambda x:x*3,num))
print(result)

# Convert string to uppercase
str = ["priya","ram","seetha"]
result = list(map(lambda x :x.upper(),str))
print(result)

# get length of each string
str = ["priya","ram","seetha"]
result = list(map(lambda x:len(x),str))
print(result)


# add 5 to each salary
nums = [5000,2000,3000,1000]
result = list(map(lambda x:x+5,nums))
print(result)


# extract first character
str = ["priya","ram","seetha"]
result = list(map(lambda x:x[0],str))
print(result)



# Filter

# number>10
num =[10,3,8,20,5,16,23,9]
result = list(filter(lambda x:x>10,num))
print(result)


# word startwith p
str = ["priya","ram","seetha","param"]
result = list(filter(lambda x:x.startswith('p'),str))
print(result)

# odd numbers
num =[10,3,8,20,5,16,23,9]
result=list(filter(lambda x:x%2==1,num))
print(result)


# name longer than 4 chars
str = ["priya","ram","seetha","param","sam"]
result=list(filter(lambda x:len(x)>4,str))
print(result)


# reduce

# sum
from functools import reduce
nums = [1,2,3,4,5,6,7,8]
result = reduce(lambda x,y :x+y,nums)
print(result)

# product
nums = [1,2,3]
result = reduce(lambda x,y :x*y,nums)
print(result)

# maximum
nums=[10,20,30,40,50]
result = reduce(lambda x,y:x if x>y else y,nums)
print(result)

# minimum
nums=[10,20,30,40,50]
result = reduce(lambda x,y:x if x<y else y,nums)
print(result)



str=["hello","priya"]
result = reduce(lambda x,y:x+y,str)
print(result)




# Sorted

nums = [5,1,3,2]
print(sorted(nums))



nums = [5,1,3,2]
print(sorted(nums,reverse=True))
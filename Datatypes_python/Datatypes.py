# STRING
# name = "Priya"
# msg = 'Hello'

# print("priya".upper())

# print("HELLO".lower())

# print("  hi  ".strip())

# print("hello world".replace("world", "Priya"))

# print("a,b,c".split(","))

# print("-".join(["a","b","c"]))


# LIST
# fruits = ["apple", "banana", "mango"]
# numbers = [1, 2, 3]

# fruits = ["apple"]
# fruits.append("banana")
# print(fruits)


# fruits.extend(["mango", "grapes"])
# print(fruits)

# fruits.insert(1, "kiwi")
# print(fruits)

# nums = [3,1,4,2]
# nums.sort()
# print(nums)

# fruit = ["apple", "banana", "mango"]
# fruit.pop()
# print(fruit)

# fruitss = ["apple", "banana", "mango"]
# fruitss.pop(1)
# print(fruitss)


# nums.reverse()
# print(nums)

# nums.clear()
# print(nums)


# TUPLE
# t1 = (1, 2, 3)
# t2 = "a", "b", "c"
# t3 = 10,

# t = (1, 2, 3, 4, 2, 7)
# print(t.count(2))

# print(t.index(4))


# Set

# my_set = {1, 2, 3}
# print(my_set)

# my_set = set()

# s = {1, 2, 2, 3}
# print(s)

# s = {1, 2}
# s.add(3)
# print(s)

# s = {1, 2}
# s.update([3, 4])
# print(s)

# s = {1, 2, 3}
# s.remove(2)
# print(s)

# s = {1, 2, 3}
# s.discard(5)   # no error
# print(s)

# s = {10, 20, 30}
# s.pop()
# print(s)

# s = {1, 2, 3}
# s.clear()
# print(s)

# a = {1, 2}
# b = {2, 3}
# print(a.union(b))

# a = {1, 2, 3}
# b = {2, 3, 4}
# print(a.intersection(b))

# a = {1, 2, 3}
# b = {2, 3}
# print(a.difference(b))


# a = {1, 2}
# b = {2, 3}
# print(a.symmetric_difference(b))


# Dictionary

# student = {
#     "name": "Priya",
#     "age": 22,
#     "course": "Python"
# }
# print(student)

# student = {"name": "Priya", "age": 22}
# print(student["name"])

# print(student.get("city"))

# student = {"name": "Priya"}
# student["city"] = "Bengaluru"
# print(student)

# student = {"name": "Priya", "age": 21}
# student["age"] = 22
# print(student)

# student = {"name": "Priya", "age": 22}
# student.pop("name")
# print(student)


# student = {"name": "Priya", "course": "Python"}
# student.popitem()
# print(student)


# student = {"name": "Priya", "age": 22}
# del student["name"]
# print(student)


# student = {"name": "Priya"}
# student.clear()
# print(student)


# student = {"name": "Priya", "age": 22}
# print(student.keys())
# print(student.values())
# print(student.items())

# a = {"name": "Priya"}
# b = {"age": 22}
# a.update(b)
# print(a)
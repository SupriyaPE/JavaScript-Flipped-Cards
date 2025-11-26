import copy

list1 = ["A", "B", [10, 20]]
list2 = copy.copy(list1)  # shallow copy
list3 = copy.deepcopy(list1)  # deep copy
list4 = list1

list2[2][0] = "shallow"
list3[2][0] = "deep"


list1.append(100)

print(list1)  # original
print(list2)  # shallow copy
print(list3)  # Original
print(list4)


print(id(list1))
print(id(list2))
print(id(list3))
print(id(list4))



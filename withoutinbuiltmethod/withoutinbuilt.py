# arr =[10,20,5,8,15,7,32,12,0,6,19]

# min_val = arr[0] 
# for i in arr:
#     if i<min_val:
#         min_val=i

# print("minimum",min_val)



# max_val = arr[0] 
# for i in arr:
#     if i>max_val:
#         max_val=i

# print("maximum",max_val)



# for i in range(1,11):
#     print("2*",i,"=", 2*i)



# arr =[10,20,5,8,15,7,32,12,0,6,19]

# last_value = arr[-1]
# print("last value:",last_value)   



arr =[0,5,0,10,0,8]

result = []
for i in arr:
    if i!=0:
        result.append(i)
    
zeros = arr.count(0)
for j in range(zeros):    
   result.append(0)
print(result)




arr =[0,5,0,10,0,8]
result=[]

for i in arr:
    if i!=0:
        result.append(i)

zerostoend = len(arr) - len(result)
for j in range (zerostoend):
    result.append(0)

print(result)



arr =[0,5,0,10,0,8]
result=[]

for i in arr:
    if i!=0:
        result.append(i)

while len(result)<len(arr):
    result.append(0)
print(result)    




arr =[0,5,8,3,0,10,5,0,8]
result=[]
for i in arr:
    if i not in result:
        result.append(i)
print(result)     




arr =[0,5,8,3,0,10,5,0,8]
freq={}
for i in arr:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1
print(freq)        



arr =[5,8,3,0,10]
rev =[]
for i in range(len(arr)-1,-1,-1):
    rev.append(arr[i])
print(rev)    




arr =[3,10,5,8,12,20]
first = second = 0
for i in arr:
    if i> first:
        second=first
        first =i
    elif i>second and i!=first:
        second = i
print(second)            




arr =[10,20,10]

if arr == arr[::-1]:
    print("palindrome")
else:
    print("not palindrome")    

    
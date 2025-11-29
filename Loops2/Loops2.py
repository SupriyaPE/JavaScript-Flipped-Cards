# user_input =""
# while user_input != "stop":
#     user_input = input("Type Something :")


# attemps = 0

# while attemps < 3:
#     psw = input("enter password: ")
#     if psw == "admin":
#         print("login successful") 
#         break
#     else:
#         print("wrong password")
#     attemps+=1
# else:
#     print("try later")


# while True:
#     num = int(input("enter positive num:"))
#     if num>0:
#         print("Good")
#     else:
#         print("invalid num")
#         break


# countries = ["IND","CHINA","SL","BAN"]
# for data in countries:
#     countries.pop()
#     print(data)
#     print(countries)

# print("countries ==>> ",countries)



# countries = ["IND","CHINA","SL","BAN"]
# for data in countries:
#     print(data)
#     countries.pop()
#     print("length ===>>",len(countries))



# countries = ["IND","CHINA","SL","BAN"]

# for i,data in enumerate(countries):
#     try:
#         start_server()
#     except:
#         print(f"Could not start this {data} server")
#         send_mail()
#         break
# else:
#     print("All the servers started successfully")


# for i in range(5):
#     print(i)
# else:
#     print("no block occured")


# for i in range(5):
#     print(i)
#     if i == 4:
#      break
# else:
#     print("no block occured")



# num = ["xyz",10,20,"abc","30" "10A"]

# for n in num:
#     try:
#         val=int(n)
#     except:
#         print("invalid number:",n)
#     else:
#         print("coverted:",val)



# attempts = 0

# while attempts < 3 :
#     psw=input("Enter password:")
#     if psw =="admin":
#         print("login successful")
#         break
#     else:
#         print("wrong psw")
#         attempts += 1
# else: 
#     print("try later")


# while True:
#     num = int(input("Enter Positive number:"))
#     if num>0:
#         print("Good")
#     else:
#         print("Invalid")
#         break



# i = 1
# while i<=3:
#     j = 1
#     while j <= 2:
#         print(i,j)
#         j+=1
#     i+=1



# num = 3
# i = 1
# while i<=10:
#     print(num,"x",i,"=", num*i)
#     # print(f"{num} x {i} = {num * i}")
#     i+=1



# i=0
# while i<3:
#     j=1
#     while j<2:
#         print(i,j)
#         j+=1
#     i+=1    
     


# i=1
# while i<=5:
#     j=1
#     while j<=5:
#         print("*",end=" ")
#         j+=1
#     print()
#     i+=1


# for i in range(5,0,-1):
#     print(i)

# for row in range(1,4):
#     for col in range(1,4):
#         print(row,col)


# for i in range(1,6):
#     if i==3:
#         pass
#     print(i)



# result = []
# for i in range(5):
#     result.append(i*2)

# print(result)    


# result = [i*2 for i in range(5)]
# print(result)
# def multifly(n):
#     def inner(x):
#         return x*n
#     return inner

# product = multifly(2)
# print(product(5))



# def outer():
#     x = 10
#     def inner():
#         return x * 2
#     return inner
# func = outer()
# print(func())



# count =100
# def counter():
#     count = 10
#     def inc():
#         # count = 20
#         # global count
#         nonlocal count
#         count+=1
#         return count
#     return inc
# func=counter()
# print(func())



# def discount_generaror(perscent):
#     def apply_discount(amount):
#         return amount - (amount*perscent/100)
#     return apply_discount

# festival_discount = discount_generaror(10)
# member_discount = discount_generaror(20)

# print(festival_discount(1000))
# print(member_discount(1000))



# def decorator(func):
#     def wrapper():
#         print("Before")
#         func()
#         print("After")
#     return wrapper    

# @decorator 
# def greet():
#     print("hello")
# greet()    

# @decorator
# def check():
#     print("Checked")
# check()    
    


# def login_required(func):
#     def wrapper():
#         print("checking user login")
#         user_logged_in = True
#         if user_logged_in:
#           return func()
#         else:
#             print("login denaid,login first")
#     return wrapper    

# @login_required
# def dashboard():
#     print("welcome to dashboard")   
# dashboard()
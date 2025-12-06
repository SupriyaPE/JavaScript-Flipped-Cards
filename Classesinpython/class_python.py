# # Class # #
# class Car:
#     def start(self,brand,color = "Red"):
#         self.brd = brand
#         self.clr = color
#         print("Car started")

# car1 = Car()
# car2 = Car()

# car1.start("Audi")
# car2.start("Thar")



# class Vehicle:
#     def __init__(self, brand, color="red"):
#         self.brd = brand
#         self.clr = color

# car1 = Vehicle("Audi")
# car2 = Vehicle("Thar","Black")

# print(car1.clr)
# print(car2.clr)



# class Vehicle:
#     def __init__(self, brand, color="red"):
#         self.brd = brand
#         self.clr = color
#         self.move = "yes"

# car1 = Vehicle("Audi")
# car2 = Vehicle("Thar","Black")

# print(car1.move) 
# print(car2.move)



# class Vehicle:
#     def __init__(self, brand, year, color="red"):
#         self.brd = brand
#         self.yr = year
#         self.clr = color

# class Car(Vehicle):
#     def __init__(self, brand, year):
#         super().__init__(brand, year)


# class Plane(Vehicle):
#     def __init__(self, brand, year):
#         super().__init__(brand, year, "NA")



# car1 = Car("Audi",2025)
# plane1 = Plane("Indigo",2020)

# print(car1.clr)
# print(plane1.clr)



# class Vehicle:
#     def __init__(self,brand,year,color="red"):
#         self.brd = brand
#         self.yr = year
#         self.clr = color
    
#     def move(self):
#         print("I just move")
    

# class Car(Vehicle):
#     def __init__(self, brand, year, color="red"):
#         super().__init__(brand, year, color)

#     def move(self):
#         print("I move on Road")
 
    
#     def changeColor(self,color):
#         self.clr=color

# class Plane(Vehicle):
#     def __init__(self, brand, year, color="red"):
#         super().__init__(brand, year, color)

#     def move(self,clr):
#         self.color = clr
#         print("I move on air")


# v1=Vehicle("volvo",2023)
# car1=Car("audi",2020)
# pln1=Plane("indigo",2021)

# print(car1.clr)
# car1.changeColor("white")
# print(pln1.yr)


# v1.move()
# car1.move()
# pln1.move()
        




# class Vehicle:
#     def __init__(self,brand,year):
#         self.brd = brand
#         self.yr = year
     
    
#     def move(self):
#         print("I just move")



# class Car(Vehicle):
#     def __init__(self, brand, year):
#         super().__init__(brand, year)
#         self.color ="white"

#     def move(self):
#         print("I move on Road")
 
    
#     def changeColor(self,clr):
#         self.color=clr


# v1 = Vehicle("vovlo",2023)
# car1 = Car("audi",2024)
# car2 = Car("Thar",2020)


# print(car1.color)
# print(car2.color)

# car2.changeColor("Red")


# print(car1.color)
# print(car2.color)
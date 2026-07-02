# class Dog:
#         def __init__(self,name,age):
#             """initialize name and age attribute"""
#             self.name=name
#             self.age=age
#         def sit(self):
#             print(f"{self.name} is now sittinng")
#         def roll_over(self):
#              print(f"{self.name} rolled over!")
# my_dog=Dog('marco',1)
# my_dog.sit()
# my_dog.roll_over()



#try it yourself
# class Restaurant:
#     def __init__(self,restaurant_name,cuisine_type):
#         self.restaurant_name=restaurant_name
#         self.cuisine_type=cuisine_type
#     def describe_restaurant(self):
#         print(f"{self.restaurant_name} is the name of the restaurant")
#         print(f"{self.cuisine_type} is the special cusine we have.")
#     def open_restaurant(self):
#         print(f"{self.restaurant_name} is open now.")

# rest=Restaurant('baba ka dhaba','panjabi')
# rest.describe_restaurant()
# rest.open_restaurant()


# class User:
#     def __init__(self,first_name,last_name,age):
#         self.first_name= first_name
#         self.last_name= last_name
#         self.age= age
#     def describe_user(self):
#         print(f"{self.first_name} {self.last_name} is my name.my age is {self.age}")
#     def greet_user(self):
#         print(f"{self.first_name.title()} {self.last_name.title()},good morning")
# user=User('anmol','mishra',21)
# user.describe_user()
# user.greet_user()

# class Car:
#     def __init__(self,make,model,year):
#         """initialize attributees to describe a car"""
#         self.make=make
#         self.model=model
#         self.year=year
#         self.odometer_reading=0
        
#     def read_odometer(self):
#         print(f"This car has {self.odometer_reading} mileage.")
# my_new_car=Car('audi','a4',2024)
# my_new_car.odometer_reading=23
# my_new_car.read_odometer()

# class Dog: #class,captial first letter, blue print
#     def __init__(self,name,age): #initalization ,construstor,inint method,automatically run when ever instance is created from class
#         """features of dog"""
#         self.name=name
#         self.age=age
    
#     def sit(self):
#         """siumlate a dog sitting in response of a commanad"""
#         print(f"{self.name} is now sitting")
    
#     def roll_over(self):
#         """simulate rolling over in response to a command"""
#         print(f"{self.name} is now rollimg")

# my_dog = Dog('marco',6)
# # my_dog.sit()
# # my_dog.roll_over()        
# print(f"my dog's name is {my_dog.name}")
# print(f"my dog is {my_dog.age} years old")

# class Car:
#     """A simple attempt to represent a car"""
#     def __init__(self,make,model,year):
#         """Initialize attributes to describe a car."""
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0
#     def get_descriptive_name(self):
#         """Return a neatly formatted descriptive name."""
#         long_name = f"{self.year} {self.make} {self.model}"
#         return long_name.title()
#     def read_odometer(self):
#         """print to show caar mileage"""
#         print(f"This car has {self.odometer_reading} miles on it.")

# my_new_car = Car('audi', 'a4', 2024)
# print(my_new_car.get_descriptive_name()) 
# my_new_car.odometer_reading = 23
# my_new_car.read_odometer()       


# class Restaurant:
#     def __init__(self,restaurant_name,cuisine_type):
#         self.restaurant_name=restaurant_name
#         self.cuisine_type=cuisine_type
#         # self.number_served = 0
#     def describe_restaurant(self):
#         print(f"{self.restaurant_name} is the name of the restaurant")
#         print(f"{self.cuisine_type} is the special cusine we have.")
#     def open_restaurant(self):
#         print(f"{self.restaurant_name} is open now.")
#     def set_number_served(self,number):
#         """to check number served"""
#         self.number=number
#         print(f"The number of customer servesd is {self.number}")




# rest=Restaurant('baba ka dhaba','panjabi')
# rest.describe_restaurant()
# rest.open_restaurant()

# rest.set_number_served(23)

# restaurant = Restaurant('syanko', 'chinese')
# print(f"Today we serve {restaurant.number_served} customer.")

# restaurant.number_served = 20
# print(f"Today we serve {restaurant.number_served} customer.")


# class User:

#     def __init__(self,first_name,last_name,age,login_attempts):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
#         self.login_attempts = login_attempts

#     def describe_user(self):
#         print(f"{self.first_name} {self.last_name} is my name.my age is {self.age}")

#     def greet_user(self):
#         print(f"{self.first_name.title()} {self.last_name.title()},good morning")

#     def increment_login_attmpts(self):
#         """check increment value of login"""
#         self.login_attempts += 1
#         print(f"{self.login_attempts}")

#     def reset_login_attempts(self):
#        """rest logim"""
#        self.login_attempts *= 0
#        print(f"{self.login_attempts}")


# user=User('anmol','mishra',21,1)
# user.describe_user()
# user.greet_user()

# user.increment_login_attmpts()
# user.increment_login_attmpts()
# user.increment_login_attmpts()
# user.increment_login_attmpts()
# user.increment_login_attmpts()
# user.increment_login_attmpts()
# user.increment_login_attmpts()

# user.reset_login_attempts()

# class Car:
#     """A simple attempt to represent a car."""

#     def __init__(self, make, model, year):
#         """Initialize attributes to describe a car."""
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0

#     def get_descriptive_name(self):
#         """Return a neatly formatted descriptive name."""
#         long_name = f"{self.year} {self.make} {self.model}"
#         return long_name.title()

#     def read_odometer(self):
#         """Print a statement showing the car's mileage."""
#         print(f"This car has {self.odometer_reading} miles on it.")

#     def update_odometer(self, mileage):
#         """Set the odometer reading to the given value."""
#         if mileage >= self.odometer_reading:
#             self.odometer_reading = mileage
#         else:
#             print("You can't roll back an odometer!")

#     def increment_odometer(self, miles):
#         """Add the given amount to the odometer reading."""
#         self.odometer_reading += miles

# class ElectricCar(Car):
#     """Represent aspects of a car, specific to electric vehicles."""
#     def __init__(self, make, model, year):
#         """Initialize attributes of the parent class."""
#         super().__init__(make, model, year)


# my_leaf = ElectricCar('nissan', 'leaf', 2024)
# print(my_leaf.get_descriptive_name())

# from random import randint
# result=randint(1,6)
# print(result)




# class Dog:
#     # Class attribute (shared by all instances)
#     species = "Canis familiaris"
    
#     # Constructor (initializer)
#     def _init_(self, name, age):
#         # Instance attributes (unique to each instance)
#         self.name = name
#         self.age = age
        
    
#     # Instance method
#     def bark(self):
#         return f"{self.name} says woof!"
    
#     # Another instance method
#     def get_age(self):
#         return f"{self.name} is {self.age} years old."
    
    

# # Creating instances (objects) of the Dog class
# dog1 = Dog("Buddy", 3)
# dog2 = Dog("Charlie", 5)

# #Accessing attributes and methods



# print(dog1.bark())         # Buddy says woof!
# print(dog2.get_age())      # Charlie is 5 years old.
# print(dog1.species)        # Canis familiaris
# print(dog1.age())






from dog import Dog
from cat import Cat

dog1= Dog ("d1",3)
cat1=Cat("c1",4)

print(dog1)
print(cat1)
# # class Animal:
   
# #     def __init__(self, name, age):
       
# #         self.name = name
# #         self.age = age
# #         self.__age =age #private
    
   
# #     def get_age(self):
# #         return f"{self.name} is {self.age} years old."
    
    
# #     def __str__(self):
# #         return f"\n name{self.name}\nname is {self.age} \n"


# # dog1= Dog("d1",3)
# # cat1= Cat("c1",4)



# from animal import Animal

# class Dog (Animal):
#     def bark(self):
#         return f"{self.name}says woof!"
    



# from animal import Animal
# class Cat (Animal):
#     Species = "cat sapcies"

#     def neu (self):
#         return f"{self.name}"




# #define class method and static method in python with example.



import matplotlib.pyplot as plt

# Data for plotting
x = [1, 2, 3, 4]
y = [10, 20, 25, 30]

# Create a simple line plot
plt.plot(x, y)
plt.title("Basic Line Plot")
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.show()
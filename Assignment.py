# name = input("Enter your Name ")
# rev = " " # used to store the reverse value 
# for i in name: # using for loop for to reverse the 
#  rev = i+rev
# print(rev)   



# a = int (input(" Enter your first number  ")) # user input for integer
# b = input(" Enter your second number  ") # user input for float
# c = input(" Enter your third number  ") # user input for complex
# print(type(a),a) # type casting integer

# b = float(a)  # type casting float
# print(type(b),b,c)

# c = complex(a) # type casting complex
# print(type(c))




# num_1 = float(input("Enter length of area ")) # input the value of area of length
# num_2 = float(input("Enter width of area ")) # input the value of area of width
# area = num_1 * num_2 
# print("area of rectangle :" , area)  # print the total area using print function 


# area = num_1 * num_2
# float_area = format(area,".2f")
# print(f"area of the rectangle is {float_area}")


# A = int(input("Enter your first number "))
# B = int(input("Enter your second number "))
# C = int(input("Enter your third number "))

# avg = (A+B+C)/3

# print("Average is % 2f : " % avg)


for i in range(1, 4):
 num = int(input("Enter Your number  "))
 if(num==0):
     print ( "This value is zero " ,a )
 elif(num>0):
     print("This is pos ++ value " ,a ) 
 elif(num<0):
     print("This is neg -- value " ,a )
 else:
     print("Enter the valid number ")

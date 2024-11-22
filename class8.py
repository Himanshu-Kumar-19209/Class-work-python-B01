# write a program to create a list of squares of number from  0 to n using list comrehension

n = 50 
res = [x**2 for x in range(0,n) if x  % 2 == 0]
print (res)


# wap to create a dictionary comrehension keys are value 


res1 = { x:x**2 for x in range(0,n) if x % 2==0 }

print (res1)

# WA. unction that take dictionary argument and return where keys are  value 


def flip_dictionary(d1):
    assert isinstance(d1, dict), "Input is not a dictionary "
    flipped = {val :key for key, val in d1.items()}

    return flipped


print(f"flipped dictionary is \n{flip_dictionary(res1)}")

flip_dictionary(1)
# Write a function  that takes one input parameter (n) and evaluats an expression a = n * 10, for all values between 0 to n
import time 
n = 100000
def testfn(n):
    for i in range (0, n):
        a =i * 10

#extimate execution time of this function for n

start_time =time.time()  * 100000
#print (start_time)

testfn(n)
end_time =time.time() *100000
#print(end_time)
print(f"For n = {n} \n Execution time is{end_time - start_time} micro seconds")

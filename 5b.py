import time 
ns = [1234123, 1234532, 1234231, 2314231]
n = 1000000


def testfn(n):
    for i in range (0, n):
        a =i * 10

#extimate execution time of this function for n
def wrapper (func,*args, **kwargs):
  def wrapper(*args, **kwargs):
     start_time =time.time()  * 100000
     
     func(*args, **kwargs)
  
     end_time=time.time() *100000
    
     print(f"For n = {n} \n Execution time is{end_time - start_time} micro seconds")

  return wrapper
  
n = 10000000

wrapped_fn = wrapper (testfn,n)

wrapped_fn(n)
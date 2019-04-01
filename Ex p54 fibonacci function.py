def fib(n):
    """Assumes n int >= 0
        Returns Fibonacci of n"""
    if n ==0 or n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
        
def testFib(n):
        for i in range(n+1):
            print('fib of', i, '=', fib(i))
            
#Question: When fib is used to compute fib(5), how many times does it compute the value of fib(2) on the way to computing fib(5)? 
#Answer: Three times.

#Explanation: 

#When asked for fib(5), it computes fib(4) and fib(3) and adds these. Break into cases: 

#CASE OF fib(4): In computing fib(4), it asks for fib(3) and fib(2) and adds these. 
#SUBCASE of fib(3): In computing fib(3), it asks for fib(2) and fib(1) and adds these. 
#That makes two computations of fib(2) while computing fib(4). 

#CASE OF fib(3): In computing fib(3), it asks for fib(2) and fib(1) and adds these. That makes one computation of fib(2) while computing fib(3). 

#So we have two computations of fib(2) while computing fib(4) and one while computing fib(3). That makes three computations of fib(3). 



#Different answer: Once. It starts by computing fib(0) and fib(1) and then computes fib(n) once for each 1 < n <= 5, using each time the previous two computations. 
#Given a number N find the sum of all the even valued
#terms in the fibonacci sequence less than or equal to N.
#Try generating only even fibonacci numbers instead of iterating over all
#Fibonacci numbers
#Input number : 8
#Output:10

n = int(input("Enter the value of n:"))
def sum_even_fib(n):
    sum = 0
    if(n <= 1):
        return sum
    fib1,fib2 = 1,1
    while(fib2 <= n):
        if(fib2 % 2 == 0):
            sum += fib2
        fib1,fib2 = fib2,fib1 + fib2
    return sum
print(sum_even_fib(n))

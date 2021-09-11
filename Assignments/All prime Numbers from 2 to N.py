#You are given an input integer N, and you have to print all the prime
#numbers between 2 to N (both inclusive) in different lines.
#For example, if the given number is 7, then the prime numbers between 2 to 7 will be 2,3,5 and 7
#which must be printed in different lines in the output.

n = int(input("Please enter a number:"))

def isPrime(n):
    prime = True
    for i in range(2,n):
        if(n % i == 0):
            prime = False
            break
    return prime


for j in range(2,n+1):
    if(isPrime(j)):
        print(j)


    

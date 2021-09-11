#find and return number of trailing 0s in n factorial
#without calculation n factorial
n = int(input("Please enter a number:"))
def trailingZeros2(n):
    result = 0 
    power = 5 
    while(n >= power):
        result += n // power
        power *= 5
    return result


print(trailingZeros2(n))


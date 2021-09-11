#Given a decimal number (integer N),you have to convert it into binary
#and print it. The binary number should be printed in the form of an integer.
#For example, if the given decimal number is 12,then the corresponding binary number will be
#1100, and we need to print it.

n = int(input("Please enter the number:"))      #take a number from user
binary_num = 0                                  #binary number which we will get                      
place = 1                                       #place reconizer
while( n!=0 ):  
    rem = n%2                                           #remainder
    binary_num = rem * place + binary_num               #binary_number which we are getting 
    place = place * 10                                  #increasing the place value
    n = n//2                                            #Dividing the number by 2 

print(binary_num)            #printing the final binary number


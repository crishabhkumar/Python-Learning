#Given a decimal number (integer N),you have to convert it into Octal
#and print it. The Octal number should be printed in the form of an integer.

n = int(input("Please enter the number:"))          #taking the number from user
octal_num = 0                                       #intialization of ocatl number
place = 1                                           #for recongniztion of place
while(n!=0):        
    rem = n%8                                   #getting remainder
    octal_num = place * rem + octal_num         #getting ocatl number
    place = place * 10                          #increasing place value
    n = n // 8                                  #dividing the number by 8

print("Octal Number is:",octal_num)             #finally printing the number

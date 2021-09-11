#Problem Description: You are given with an input number N, then you have to print the given
#star pattern corresponding to that number N.
#For example, if N=4
#Pattern output:
#1      1
#12    21
#123  321
#12344321

#For N=5, the pattern output would be:
#1        1
#12      21
#123    321
#1234  4321
#1234554321

n = int(input("Please enter the totalnumber of rows:"))

row = 1
while(row <= n):
    col = 1
    num1 = 1
    num2 = row
    while(col <= 2*n):
        if(col <= row):
            print(num1,end="")
            num1 += 1
        elif(col >= row +1 and col <= 2*n - row):
            print(" ",end = "")
        else:
            print(num2,end = "")
            num2 -= 1
        col += 1
    row += 1
    print()


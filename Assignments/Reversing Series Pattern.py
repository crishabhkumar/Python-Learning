n = int(input("Enter the value of n:"))


''' Print n lines in a specic pattern. The numbers starts from 1 and
keeps on increasing. There are i numbers on ith line. The numbers on even
lines are in decreasing order. '''
def printlines(n):
    row=1               #intializing row with first line
    i=0                 #the number which will increase continuously
    col = 1             #the col
    while(row<=n):
        if(row%2==0):   #if row is even then it will start printing in decreasing order 
            col = -1
            i += row-1
        else:           #if row is odd the it will start printing in increasing order
            col = 1
            i += row
        # print line
        for loop in range(0,row):   #this loop is helping in to print the values in increasing or decreasing order
            print (i, end=' ')
            i += col
        print()
        row += 1


printlines(n)


#Selection Sort
lis = [2,45,14,15,10,9,1,42]
n = len(lis)
for i in range(n):
    #small = lis[i]
    for j in range(i+1,n):
        if(lis[j] < lis[i]):
            temp = lis[i]
            lis[i] = lis[j]
            lis[j] = temp

print(lis)










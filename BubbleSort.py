#Bubble Sort
lis = [3,2,4,15,12,10]
n = len(lis)
print(lis)
for j in range(n - 1):
    for i in range(0, n - 1 - j):
        if(lis[i] > lis[i + 1]):
            temp = lis[i]
            lis[i] = lis[i + 1]
            lis[i + 1] = temp
    
print(lis)




n= int(input())
arr = list(map(int,input().split()))
temp = [0]*100
for i in range (n):
    x = arr[i]
    temp[x] += 1
for i in range(len(temp)) :
    if temp[i] != 0:
        for j in range(temp[i]):
            print(i,end=' ')

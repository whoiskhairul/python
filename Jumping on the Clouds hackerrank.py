n = int(input())
arr = list(map(int,input().split()))
arr.append(2)
arr.append(2)
i=0
count = 0
while i<n :
    if( arr[i + 2] == 2) and arr[i + 1] != 0:
        x = 0
        i = i + 2
    elif arr[i + 2] ==1:
        x = 0
        count+=1
        i = i + 1
    elif( arr[i + 2] == 0 ):
        count+=1
        i= i + 2
        x = 0
    elif (arr[i + 1] == 0):
        count += 1
        i = i + 1
        x = 0

print(count)

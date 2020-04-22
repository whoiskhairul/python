arr = []
max = -99999
for i in range(6):
    arr.append(list(map(int, input().split())))
for i in range(4):
    for j in range(4):
        sum = 0
        sum = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1] + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
        if(sum>max):
            max = sum
print(max)


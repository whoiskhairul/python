n = int(input())
arr = []
for i in range(n):
    name = input()
    score = float(input())
    arr.append([score,name])
arr = sorted(arr)
s = arr[0][0]
while (arr[0][0] == s ):
    arr.pop([0][0])
s = arr[0][0]
for i in range(len(arr)):
    if(arr[i][0] == s ):
        print(arr[i][1])
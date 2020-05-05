n = int(input())
s = 101
arr = []
for i in range(n):
    name = input()
    name = name + ' '
    score = float(input())
    arr.append([name,score])
for i in range(n):
    if arr[i][1] < s :
        s = arr[i][1]
for i in range(n):
    if arr[i][1] == s :
        arr[i].pop()
        arr[i].pop()
s = 101
arr = [x for x in arr if x != []]

for i in range(len(arr)):
    if arr[i][1] < s :
        s = arr[i][1]
        result = ''
        result = result + arr[i][0]
    elif arr[i][1] == s:
        result = result+arr[i][0]
arr = sorted(result.split())
for i in range(len(arr)):
    print(arr[i])


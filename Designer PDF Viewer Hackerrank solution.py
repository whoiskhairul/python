import string

s = string.ascii_lowercase
arr = list(map(int, input().split()))
pdf = input()
max = -1
for i in range(len(pdf)):
    n = s.index(pdf[i])
    m = arr[n]
    if (m > max):
        max = m
print(max * len(pdf))

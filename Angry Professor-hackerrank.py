t = int(input())
a = []

for i in range(t):
    count = 0
    n, k = input().split()
    n = int(n)
    k = int(k)

    # x = int(input().split())
    a = input().split()
    for j in range(n):
        a[j] = int(a[j])
        if (a[j] < 1):
            count += 1

    if (count < k):
        print("YES")
    else:
        print('NO')

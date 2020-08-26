for i in range(int(input())):
    n = int(input())
    mod = n%5
    if n>=40 and mod>2:
        print(n-mod+5)
    else:
        print(n)
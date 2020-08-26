import math


# Complete the encryption function below.
def encryption(s):
    s = s.replace(" ", "")
    length = len(s)
    m = math.isqrt(length)
    n = math.sqrt(length)
    if m != n:
        p = m + 1
    list = [p]
    r = []
    i = 0
    j = 0
    while i <= length:
        list[j] = s[i: i + p:]
        i = i + p
        j = j + 1
    for x in list:
        for y in list:
            r[x] = r + list[y][x]
    print(r)


if __name__ == '__main__':
    s = input()

    result = encryption(s)

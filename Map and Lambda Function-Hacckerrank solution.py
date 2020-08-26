cube = lambda x: x * x * x


def fibonacci(n):
    ar = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377]
    arr = []
    for i in range(n):
        arr.append(ar[i])
    return arr


if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))

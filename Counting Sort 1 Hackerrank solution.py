from collections import Counter


def countingSort(arr):
    c = Counter(arr)
    dict(c)
    i = 0
    for i in range(100):
        if i in c:
            print(c[i], end=' ')
        else:
            print('0', end=' ')


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    result = countingSort(arr)


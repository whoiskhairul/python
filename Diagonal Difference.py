def diagonalDifference(arr):
    l = len(arr)
    l_to_r = 0
    r_to_l = 0
    for i in range(l):
        l_to_r += arr[i][i]
        r_to_l += arr[i][l-i-1]
    return abs(l_to_r-r_to_l)


if __name__ == '__main__':
    n = int(input().strip())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)
    print(result)
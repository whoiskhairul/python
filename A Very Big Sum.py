def aVeryBigSum(ar):
    count = 0
    for i in ar:
        count += i
    return count


if __name__ == '__main__':
    ar_count = int(input())
    ar = list(map(int, input().rstrip().split()))
    result = aVeryBigSum(ar)
    print(result)

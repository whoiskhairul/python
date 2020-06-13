def miniMaxSum(arr):
    arr.sort()
    min_sum,max_sum = 0,0
    for i in range(len(arr)-1):
        min_sum+= arr[i]
    for i in range(1,len(arr)):
        max_sum+= arr[i]
    print(min_sum,max_sum)
if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))
    miniMaxSum(arr)

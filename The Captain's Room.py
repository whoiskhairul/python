from collections import Counter
k,arr = int(input()), input().split()
print(Counter(arr).most_common()[-1][0])

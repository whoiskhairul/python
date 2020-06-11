from collections import defaultdict
d = defaultdict(list)

n, m =list(map(int, input().split()))
for i in range(n):
    d['A'].append(input())
for i in range(m):
    d['B'].append(input())

for i in range(len(d['B'])):
    arr = []
    for j in range(len(d['A'])):
        if d['B'][i] == d['A'][j]:
            arr.append(j+1)
    if d['B'][i] in d['A']:
        print(str(' '.join(map(str,arr))))
    else:print(-1)

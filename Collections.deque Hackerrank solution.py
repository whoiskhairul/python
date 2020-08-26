from collections import deque

d = deque()

for _ in range(int(input())):
    q = input()
    if any(i.isdigit() for i in q):
        p, n = q.split()
        if p == 'append':
            d.append(n)
        elif p == 'appendleft':
            d.appendleft(n)
    elif q == 'pop':
        d.pop()
    elif q == 'popleft':
        d.popleft()
for i in range(len(d)):
    print(d[i], end=' ')

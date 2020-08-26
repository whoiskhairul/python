m = int(input())
s = set(map(int, input().split()))
n = int(input())
for i in range(n):
    q = input()
    if ('pop' in q):
        if set:
            s.pop()
    elif 'remove' in q:
        q = q.split()
        q[1] = int(q[1])
        s.remove(q[1])
    elif 'discard' in q:
        q = q.split()
        q[1] = int(q[1])
        s.discard(q[1])

print(sum(s))

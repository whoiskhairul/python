n = input()
a = set(map(int,input().split()))

for i in range(int(input())):
    q,_ = input().split()
    b = set(map(int, input().split()))
    if 'symmetric_difference_update' in q:
        a.symmetric_difference_update(b)
    elif 'difference_update' in q:
        a.difference_update(b)
    elif 'intersection_update' in q:
        a.intersection_update(b)
    elif 'update' in q:
        a.update(b)
print(sum(a))
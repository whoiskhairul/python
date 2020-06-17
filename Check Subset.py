t = int(input())
for i in range(t):
    _, a = input(), set(map(str, input().split()))
    _, b = input(), set(map(str, input().split()))
    a.difference_update(b)
    if len(a):print('False')
    else:print('True')
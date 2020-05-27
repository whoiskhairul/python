n = int(input())
arr = []
for _ in range(n):
    count = 0
    s = input()
    count = s.count(' ')

    if count ==2:
        s = s.split()
        s[1] = int(s[1])
        s[2] = int(s[2])
        arr.insert(s[1],s[2])
    elif count == 1:
        s = s.split()
        s[1] = int(s[1])
        if s[0] =='append':
            arr.append(s[1])
        else:
            arr.remove(s[1])
    elif count ==0:
        if s == 'print':
            print(arr)
        elif s== 'sort':
            arr = sorted(arr)
        elif s=='pop':
            arr.pop()
        else:
            arr.reverse()


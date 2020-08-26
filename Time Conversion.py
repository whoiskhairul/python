s = input()
first = s[:2]
last = s[len(s) - 2::]
mid = s[2:len(s) - 2:]
if last == 'AM':
    if first == '12':
        print('00' + mid)
    else:
        print(first + mid)
else:
    if first == '12':
        print(first + mid)
    else:
        print(str(int(first) + 12) + mid)

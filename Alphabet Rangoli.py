from string import ascii_lowercase

n = int(input())
s = ascii_lowercase
s = s[:n]
und = n * 2 - 1 + n * 2 - 2
p = s[n - 1]

temp = []
print(p.center(und, '-'))

for i in range(n - 2, -1, -1):
    arr = []
    arr.append(s[i])
    for j in range(i + 1, n):
        arr.insert(0, s[j])
        arr.append(s[j])
    x = '-'.join(arr).center(und, '-')
    temp.append(x)
    print(x)
if temp:
    temp.pop()
temp.reverse()
for i in temp:
    print(i)
if n != 1:
    print(p.center(und, '-'))

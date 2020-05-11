from string import ascii_lowercase
def twoStrings(s1, s2):
    b = False
    arr = []
    res = []
    for i in ascii_lowercase:
        if i in s1: arr.append(i)
        if i in s2: res.append(i)
    for i in range(len(res)):
        if res[i] in arr: b = True
    if b: print('YES')
    else: print('NO')

if __name__ == '__main__':
    q = int(input())
    for q_itr in range(q):
        s1 = input().lower()
        s2 = input().lower()
        result = twoStrings(s1, s2)


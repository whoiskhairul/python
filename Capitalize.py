def solve(s):
    x = ''
    s = s.capitalize()
    for i in range(len(s)):
        if s[i-1] == ' ':
            x = x + s[i].upper()
        else:
            x = x + s[i]
    print(x)
if __name__ == '__main__':
    s = input()
    result = solve(s)


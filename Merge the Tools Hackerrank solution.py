def merge_the_tools(string, k):
    length = len(string)
    extra = length % k
    i = 0
    while ( i< length - extra ) :
        sub = string[i:i+k]
        sub = list(dict.fromkeys(sub))
        print(''.join(sub))
        i+=k
    if (extra > 0):
        sub = string[i-k:i+extra]
        sub = list(dict.fromkeys(sub))
        print(''.join(sub))

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)

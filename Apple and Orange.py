def countApplesAndOranges(s, t, a, b, apples, oranges):
    a_count, o_count =0, 0
    for apple in apples:
        if apple+a>=s and apple+a<=t:
            a_count+=1
    for orange in oranges:
        if b+orange<=t and b+orange>=s:
            o_count+=1
    print(a_count)
    print(o_count)

if __name__ == '__main__':
    st = input().split()
    s = int(st[0])
    t = int(st[1])

    ab = input().split()
    a = int(ab[0])
    b = int(ab[1])

    mn = input().split()
    m = int(mn[0])
    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))
    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)

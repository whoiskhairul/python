def minimumBribes(q):
    q = [p - 1 for p in q]
    moves = 0
    for i, p in enumerate(q):
        if p - i > 2:
            print('Too chaotic')
            return
        for j in range(max(p - 1, 0), i):
            if q[j] > p:
                moves += 1
    print(moves)


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)

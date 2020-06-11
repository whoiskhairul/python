dictionary = []

n = int(input())
for _ in range(n):
    dictionary.append(sorted(input()))

q = int(input())
for _ in range(q):
    print(dictionary.count(sorted(input())))


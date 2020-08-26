n, k = input().split()
n = int(n)
k = int(k)
div = (k - 3) // 2
und = '.|.'
key = 1
for i in range(div, 2, -3):
    print(('-' * i) + (und * key) + ('-' * i))
    key += 2
print('WELCOME'.center(k, '-'))
key -= 2
for i in range(3, div + 1, 3):
    print(('-' * i) + (und * key) + ('-' * i))
    key -= 2

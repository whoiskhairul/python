from collections import Counter


def checkMagazine(magazine, note):
    mag = Counter(magazine)
    n = Counter(note)
    if (n - mag == {}):
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    mn = input().split()
    magazine = input().rstrip().split()
    note = input().rstrip().split()
    checkMagazine(magazine, note)

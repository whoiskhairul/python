def fun(s):
    s = s.lower()
    m = s.count('@')
    n = s.count('.')
    if (m == 1 and n == 1):
        u, x = s.split('@')
        d, e = x.split('.')
        if u and d and e:
            count = 0
            username = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                        't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7,', '8', '9', '-', '_']
            website = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                       't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7,''8', '9']
            for i in range(len(u)):
                if u[i] not in username:
                    count = count + 1
            for i in range(len(d)):
                if d[i] not in website:
                    count = count + 1
            if (len(e) > 3):
                count = count + 1
            if (count > 0):
                return False
            else:
                return True
        else:
            return False
    else:
        return False


def filter_mail(emails):
    return list(filter(fun, emails))


if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)

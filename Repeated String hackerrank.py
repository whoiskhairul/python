s = input()
n = int(input())
temp_count = s.count('a')
length = len(s)
div = n//length
count = temp_count*div
sub = n - length*div
s = s[:sub]
count = count + s.count('a')
print(count)
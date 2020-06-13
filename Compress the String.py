from itertools import groupby

s = input()
for key,value in groupby(s):
    print("("+str(len(list(value)))+", "+str(key)+")",end=' ')

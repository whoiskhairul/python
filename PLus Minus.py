n = int(input())
arr = list(map(int, input().split()))
pos_count,neg_count,zero = 0,0,0
for i in arr:
    if i == 0:
        zero+=1
    elif i>0:
        pos_count+=1
    else:
        neg_count+=1
print("%.6f"%(pos_count/n))
print("%.6f"%(neg_count/n))
print("%.6f"%(zero/n))
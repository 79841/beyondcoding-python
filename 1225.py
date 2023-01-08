import sys
input = sys.stdin.readline
x = int(input())
k = list(map(int,input().split()))
if len(k) == 1:
    print(1)
else:
    t = []

    for z in range(len(k)-1):
        j = []
        j.append(k[z])
        
        for i in range(z+1,x):
        
            if k[i] > j[-1]:
                j.append(k[i])
        t.append(len(j))
    print(t)
    print(max(t))

a = int(input())
for i in range(a):
    b = int(input())
    c = list(map(int,input().split()))
    q = 1
    d = c[0]
    for n in range(1,len(c)):
        if c[n]>d:
            d = c[n]
            q+=1
        else:
            q+=0
    print(q)

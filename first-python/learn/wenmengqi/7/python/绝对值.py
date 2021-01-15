while True:
    a = list(map(int,input().split()))
    q = []
    w = []
    if a[0] != 0:
        del a[0]
        for i in a:
            if i < 0:
                b = -i
            else:
                b = i
            q.append(b)
            e = sorted(q)
        for n in e:
            r = q.index(n)
            v = a[r]
            w.append(v)
        y = w[::-1]
        for z in y:
            print(z,end=' ')
        continue
    else:
        break

while True:
    n = int(input())
    list1 = list(map(int, input().strip().split()))[:n]
    e=[]
    for i in list1:
        if i not in e:
            e.append(i)
    print(len(e))
    e=sorted(e)
    for x in e[:-1]:
        print(x,end=' ')
    print(e[-1])

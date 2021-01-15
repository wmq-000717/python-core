a,b,c=map(int,(input().split()))
if a>b:
    if b>c:
        print(c,b,a)
    else:
        print(b,a,c)
if a<b:
    if b<c:
        print(a,b,c)
    else:
        print(c,a,b)
n=int(input())
for x in range(2,n+1):
    fg=0
    for i in range(2,x-1):
        if x%i==0:
            fg=1
            break
    if fg==0:
        print(x)
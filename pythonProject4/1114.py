n=int(input())
a=[3,4,5]
for i in range(3,n):
    b=a[i-1]+a[i-2]+a[i-3]
    a.append(b)
if n>=4:
    print(a[i])
elif n==1:
    print(3)
elif n==2:
    print(4)
elif n==3:
    print(5)


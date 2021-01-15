
sum=0
n = int(input())
for i in range(1,n+1):
    a=1
    for j in range(2,i+1):
        a = a * j
    sum=sum+a
print(sum)
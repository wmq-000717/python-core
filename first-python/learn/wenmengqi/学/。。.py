a, b = map(int,input().split())
t=a*b
while b != 0:
    r = a % b
    a = b
    b = r
print(t//a)

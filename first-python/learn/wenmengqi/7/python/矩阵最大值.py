a = list(map(int, input().strip().split()))
b = list(map(int, input().strip().split()))
c = list(map(int, input().strip().split()))
d = a + b + c
print(max(d))
if max(d) == a[0]:
    print(1)
    print(1)
if max(d) == a[1]:
    print(2)
    print(1)
if max(d) == a[2]:
    print(3)
    print(1)
if max(d) == b[0]:
    print(1)
    print(2)
if max(d) == b[1]:
    print(2)
    print(2)
if max(d) == b[2]:
    print(3)
    print(2)
if max(d) == c[0]:
    print(1)
    print(3)
if max(d) == c[1]:
    print(2)
    print(3)
if max(d) == c[2]:
    print(3)
    print(3)

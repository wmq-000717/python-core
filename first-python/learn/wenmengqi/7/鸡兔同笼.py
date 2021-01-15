

a, b = int(input().split())
for x in range(1, a):
    y = a - x
    if 2 * x + 4 * y == b:
        print(str(x))

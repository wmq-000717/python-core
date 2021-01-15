n = int(input())
a = [n] * ((2 * n) + 1)
m = n
for i in range(((2 * n) + 1) // 2):
    for s in range(i, (2 * n) + 1 - i):
        a[s] = m
    m -= 1
    for n in a:
        print(f' {n}', end='')
    print()
for x in range((((2 * n) + 1) // 2) + 1)[::-1]:
    for h in range(x, (2 * n) + 1 - x):
        a[h] = m
    m += 1
    for n in a:
        print(f' {n}', end='')
    print()

import math
m,a = map(int, input().strip().split())
b = [1] * a
u = []
b[0] = b[1] = 0
for c in range(2, int(a * 0.5) + 1):
    for d in range(2 * c, a, c):
        b[d] = 0
for v in range(1, len(b)):
    if b[v] == 1:
        b[v] = v
        u.append(v)
for w in u:
    if w >= m:
        if str(w) == str(w)[::-1]:
            print(w)

def show(d):
    for x in range(len(d)):
        for y in range(x + 1):
            print(d[x][y], end=" ")
        print()


def create(r, c):
    d = []
    a = [0] * c
    for i in range(r):
        d.append([x for x in a])
    return d


n =int(input())
d = create(n, n)
for i in range(n):
    d[i][0] = d[i][i] = 1
show(d)
for x in range(2, n):
    for y in range(1, x):
        d[x][y] = d[x - 1][y - 1] + d[x - 1][y]
show(d)

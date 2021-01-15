def show(d):
    for x in range(len(d)):
        for y in range(len(d[x])):
            print('%d' % d[x][y], end=' ')
        print()


def create(r, c):
    d = []
    a = [0] * c
    for i in range(r):
        d.append([x for x in a])
    return d


while True:
    n = int(input())
    if n == 0: break
    d = create(n, n)
    x, y = n - 1, n // 2
    d[x][y] = 1
    for i in range(2, n * n + 1):
        nx = (x + 1) % n
        ny = (y + 1) % n
        if d[nx][ny] != 0:
            nx = (x - 1 + n) % n
            ny = y
        x = nx
        y = ny
        d[x][y] = i
    show(d)
    print()

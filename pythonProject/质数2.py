t = int(input())
for i in range(t):
    a = int(input())
    b = [1] * (a + 1)
    b[0] = b[1] = 0
    q = []
    for i in range(2, a + 1):
        for j in range(2 * i, a + 1, i):
            b[j] = 0
    for i in range(a + 1):
        if b[i] == 1:
            q.append(i)
    if a in q:
        print('No')
        continue
    flat = 0
    for i in q[:-1]:
        b = a / i
        if b % 1 != 0:
            continue
        if int(b) in q:
            print("Yes")
            flat = 1
            break
    if flat == 0:
        print("No")

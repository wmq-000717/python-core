while True:
    a1, b1, c1, a2, b2, c2 = map(int, input().split())
    a = a1 + a2
    b = b1 + b2
    c = c1 + c2
    if c >= 60:
        c = c - 60
        b = b + 1
    if b >= 60:
        b = b - 60
        a = a + 1
    if a >= 24:
        a = a - 24
    print(str('%02.0f' % a) + ':' + str('%02.0f' % b) + ':' + str('%02.0f' % c))

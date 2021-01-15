n = int(input())
while n != 1:
    if n % 2 == 0:
        k = n / 2
        print("%d/2=%d" % (n, k))
        n = k
    else:
        l = n * 3 + 1
        print("%d*3+1=%d" % (n, l))
        n = l
while True:
    a, b, r = map(int, input().split())
    sum = 0
    for i in range(0, r + 1):
        c = i ** 2
        for n in range(0, r + 1):
            d = n ** 2
            if r ** 2 == c + d:
                sum += 1
    print(sum * 4 - 4)

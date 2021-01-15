while True:
    a, b = map(str, input().split())
    if a == "A" or a == "a":
        c = 10
    elif a == "B" or a == "b":
        c = 11
    elif a != "A" or a != "a":
        c = int(a)
    elif a != "B" or a != 'b':
        c = int(a)
    if b == 'A' or b == 'a':
        d = 10
    elif b == 'B' or b == 'b':
        d = 11
    elif b != 'A' or b != 'a':
        d = int(b)
    elif b != 'B' or b != 'b':
        d = int(b)
    print(c + d)

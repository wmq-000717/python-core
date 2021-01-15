Year, M = map(int,(input().split()))
if (M == 1 or M == 3 or M == 5 or M == 7 or M == 8
        or M == 10 or M == 12):
    print('31')
elif M == 4 or M == 6 or M == 9 or M == 11:
    print('0')
elif M == 2 and ((Year % 4 == 0 and Year % 100 != 0) or Year % 400 == 0):
    print('29')
else:
    print('28')

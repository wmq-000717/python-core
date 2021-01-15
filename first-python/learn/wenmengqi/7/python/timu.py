Year,Month = map(int,(input().split()))
# Month = int(input())
if (Month == 1 or Month == 3 or Month ==5 or Month == 7 or Month == 8
        or Month == 10 or Month == 12):
    print('31')
elif Month == 4 or Month == 6 or Month ==9 or Month == 11:
    print('30')
elif Month ==2 and ((Year % 4 == 0 and Year % 100 !=0 ) or Year % 400 == 0):
    print('29')
else:
    print('28')
while True:
    tot=0
    for char in input():
        if char =='8':
            tot+=2
        if char in "690":
            tot+=1
    print(tot)

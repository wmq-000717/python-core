while True:
    x=input()
    a=0
    for i in x:
        if i=='6'or i=='8':
            a=a+1
            if a>=6:
                print(x)

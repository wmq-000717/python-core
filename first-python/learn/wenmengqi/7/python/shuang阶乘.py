def doublefactorial(n):
    if n<=0:
        return 1
    else:
        return n*doublefactorial(n-2)
a = int(input())
b = (a+1)//2
for i in range(10**(b-1), 10**b):
    s = str(i)
    t = s[::-1]
    if a % 2 == 1:
        t = t[1:]
    print(s+t)
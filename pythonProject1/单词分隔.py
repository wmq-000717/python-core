a = input().split()
for i in a:
    x = ''.join(filter(str.isalnum, i))
    print(x)

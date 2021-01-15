a = []
for i in input().split():
    a.append(int(i))
b = int(input())
if (b in a):
    c = a.index(b)
    print(c)
else:
    print('Not exist')

#a = list((int, input().strip().split()))
#x = int(input())
#a.append(x)
#a.sort()
#for i in a:
    #print(type(a))
    #print(type(x))
 #   print(i)


a = []
for i in input().split():
    a.append(int(i))
b = int(input())
a.append(int(b))
for c in sorted(a):
    print(c)


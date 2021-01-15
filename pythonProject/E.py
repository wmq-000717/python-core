#import sys
#lines=sys.stdin.readlines()[1:]

n = int(input())
z1 = []
z2 = []
for i in range(n):
    a = int(input())
    if a not in z1:
        z1.append(a)
        z2.append(1)
    else:
        z2[z1.index(a)] += 1
ans1 = 0
ans2 = 0
for v in range(len(z1)):
    if z2[v] > ans2:
        ans2 = z2[v]
        ans1 = z1[v]
    if z2[v] == ans2 and ans1 > z1[v]:
        ans1 = z1[v]
print(ans1)
print(ans2)
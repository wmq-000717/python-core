n = int(input())
a = 0
c = []
while a != n:
    b = list(map(int, input().split()))
    a += 1
    c.append(b)
tot = 0

for i in range(n):
    if i != n - i - 1:
        tot += c[i][i] + c[i][n - i - 1]
    if i == n - i - 1:
        tot += c[i][i]
print(tot)

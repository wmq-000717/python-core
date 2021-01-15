n = int(input())
h = 100.0
s = 0
for n in range(0, 1001):
    s += h
    h = h / 2
print("%.4f" % s)

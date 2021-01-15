x = float(input().strip())
if x < 1:
    y = x
if 1 <= x <= 10:
    y = 2 * x - 1
if x >= 10:
    y = 3 * x - 11
print("y=""%.2f" % y)

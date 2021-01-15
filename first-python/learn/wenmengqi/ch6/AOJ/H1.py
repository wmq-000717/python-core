s = 1
n = int(input('请输入：'))
for i in range(1, n):
    s = s + 1 / (i+1)
print("%.3f" % s)

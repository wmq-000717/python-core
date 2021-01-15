n = 1235
a = ""
while n > 0:
    r = n % 10
    a = a + str(r)
    n = n // 10
print(int(a))


def sort(x):
    return int(x)

a = input().split()
a.sort(key=sort)
for i in a:
    print(i, end=" ")



a = ["a", "b", "A", "B", "1"]
a.sort()
print(a)

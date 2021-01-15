a = 1
for i in range(5):
    print("i:",i)
    if i == 2:
        continue
    a = a + 1
    print("a:",a)
else:
    print("else a:",a)
    a = a + 1
    print(a)
print(a)
print(range(5))

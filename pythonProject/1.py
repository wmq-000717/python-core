n = int(input())
list1 = []
for n in range(n):
    row = [1]
    list1.append(row)
    if n == 0:
        for num in row:
            print(num, end=" ")
            print()
        continue
    for m in range(1, n):
        row.append(list1[n - 1][m - 1] + list1[n - 1][m])
    row.append(1)
    for num in row:
        print(num, end=" ")
    print()

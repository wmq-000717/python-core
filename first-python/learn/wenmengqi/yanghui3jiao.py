N=int(input())
B = (1, 1)
for i in range(N):
    C = []
    for j in range(i + 1):
        if 1 <= j < i:
            k = B[j - 1] + B[j]
            C.append(k)
        elif j == i:
            k = B[j - 1]
            C.append(k)
        else:
            C.append(1)
    B = C
   #print(C)
new_number=C
for n in new_number:
    new_number.append(int(n))
print(new_number)

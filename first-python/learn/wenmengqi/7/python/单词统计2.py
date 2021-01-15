W = input().split()
W.sort()
print(len(W))
D = {}
for word in W:
    if word in D:
        D[word] += 1
    else:
        D[word] = 1
for w in D:
    print(w + ":" + str(D[w]))

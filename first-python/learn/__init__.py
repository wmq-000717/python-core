array=input().split()
print(array.count())

mydict = {}
for i in array:
    if i in mydict:
        mydict[i] += 1
    else:
        mydict[i] = 1

for key, value in mydict.items():
    print(key, value)
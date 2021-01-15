star=""
for i in range(1,11):
    if i<=5:
        star = star + "*"
    else:
        star = star[0:10-i]
    print(star)
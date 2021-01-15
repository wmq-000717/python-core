i = 1
star = ""
while i <= 10:
    # star=star+"*"
    if i <= 5:
        star = star + "*"
    else:
        star = star[0:10 - i]
    i = i + 1
    print(star)

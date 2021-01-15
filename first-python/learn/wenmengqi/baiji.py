# count=0
# for a in range(0,20):
#   for b in range(0,33,1):
#      c=100-a-b
#     count=count+1
#    if(a*5+b*3+c/3)==100:
#       print(a,b,c)
##break


count = 0
for i in range(0, 14):
    for j in range(25, 0, -1):
        count = count + 1
        if 7 * i + 4 * j == 100:
            print("cock=" + str(i), "hen=" + str(j), "chicken=" + str(100 - i - j))

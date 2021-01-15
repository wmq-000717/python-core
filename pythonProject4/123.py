import random

List = ["剪刀", "石头", "布"]
while 1:
    print("1:剪刀\t2:石头\t3:布")
    a = int(input())
    b = random.randint(1, 3)
    c = b - a
    print('你出的是\t', list[a - 1], '\n电脑出的是', list[b - 1])
    if c == 1 or c == -2:
        print('你输了')
        break
    elif c == 0:
        print('平局\n')
    else:
        print('你赢了,再来\n')

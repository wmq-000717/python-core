import random

while True:
    you = int(input("请出 石头(0)/剪刀(1)/布(2)"))
    com = random.randint(0, 2)
    if com == you:
        print("我出的是：%s" % you + ",计算机出的是%s" % com)
        print("心有灵犀，再来一盘！")
    elif com == you + 1 or com == you - 2:
        print("我出的是%s" % you + ",计算机出的是%s" % com)
        print("恭喜你赢了")
    else:
        print("我出的是%s" % you + ",计算机出的是%s" % com)
        print("计算机赢了。")

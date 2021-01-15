import random

player = int(input("温梦琪大笨蛋"))
computer = random.randint(0, 2)
if player == computer:
    print("我出的是：%s" % player + ",计算机出的是%s" % computer)
    print("心有灵犀，再来一盘！")
elif (player+1 == computer) or (player-2 == computer):
    print("我出的是%s" % player + ",计算机出的是%s" % computer)
    print("我赢了，计算机太弱了。")
else:
    print("我出的是：%s" % player, ",计算机出的是%s" % computer)
    print("计算机赢了")

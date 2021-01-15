amount=1000
if amount<1000:
    print("用户没有折扣，需支付的金额为：")
    print(amount)
elif 2000>amount:
        print("用户可以享受9折优惠，还需支付金额为：")
        print(amount*0.9)
elif 3000>amount:
            print("用户可以享受8折优惠，还需支付金额为：")
            print(amount*0.8)
elif amount>=3000:
            print("用户可以享受7折优惠，还需支付金额为：")
            print(amount*0.7)

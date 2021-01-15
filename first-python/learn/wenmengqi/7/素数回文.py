#


a=str(int())
b=a[::-1]
if a==b:
    while True:
        n = int(input())
        for i in range(2, n):
            if n % i == 0:
                print("不是质数")
                break
        if n == i + 1:
            print("是质数")

    print("是回文数")
else:
    print("不是")
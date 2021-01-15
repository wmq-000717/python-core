r = 10
flag = "*"
for row in range(r):
    for column in range(r):
        if row == 0 or row == r - 1:
            print(flag, end="")
        else:
            if column == 0 or column == r - 1:
                print(flag, end="")
            else:
                print(" ", end="")
    print("")

str = "字符串测试"
byteStr = str.encode()
print(str.encode())
print("加密后:",byteStr)
print("解密:",byteStr.decode())

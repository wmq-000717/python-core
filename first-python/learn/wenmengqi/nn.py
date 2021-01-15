# i=int(input("请输入第一个数字"))
#
# j=int(input("请输入第二个数字"))
#
# k=int(input("请输入第三个数字"))
# if i>j:
#     if k>i:
#         print(j,i,k)
#     elif k<j:
#         print(k,j,i)
#     else:
#         print(j,k,i)
# else:
#     if k<i:
#         print(k,i,j)
#     elif k>j:
#         print(i,j,k)
#     else:
#         print(i,k,j)
#

# 定义listNum存储输入值
listNum = []
# 循环输入
while True:
    num = int(input("输入:"));
    if -1==num:
        break;
    listNum.append(num);

# 排序list（python内置排序算法）
listNum.sort()
# 输出
print(listNum)
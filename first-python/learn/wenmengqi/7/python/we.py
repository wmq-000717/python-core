'''
x = input()
for i in x:
    if i == '1':
        x.replace('0','1')
    if i=='0':
        x.replace('1','0')
    print(x)
'''

while True:
    x=input().strip()
    for i in x:
        if i=='1':
            print(0,end='')
        else:
            print(1,end='')
    print()


while True:
    a = str(input())
    a = a.replace("0","2").replace('1','0').replace('2','1')
    print(a)
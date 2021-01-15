'''
import random
for i in range(100):
    if i != 50:
        print([random.randint(1,100)])
        continue
    break
'''
while 1:
    import random

    n = random.randint(1, 100)
    if n==50:
        print('[50]')
        break
    L=[]
    L.append(n)
    print(L,end='')
    print('这才是社区版')

#!/usr/bin/python
# -*- coding: UTF-8 -*-

x = int(input())
a = x // 10000
b = x % 10000 // 1000
c = x % 1000 //100
d = x % 100 // 10
e = x % 10
if a != 0:
    print(5)
elif b != 0:
    print(4)
elif c != 0:
    print(3)
elif d != 0:
    print(2)
else:
    print(1)

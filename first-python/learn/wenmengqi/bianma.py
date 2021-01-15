import chardet

x="温梦琪".encode("gb2312")
y=chardet.detect(x)
print(y)

# 在字符串中找出第一个只出现一次的字符

def FirstNotRepeatingchar(s):
    d = {}
    if len(s) == 0:
        return -1
    else:
        for c in s:
            if c in d:
                d[c] = d[c] + 1
            else:
                d[c] = 1
        for index, e in enumerate(list(s)):
            if d[e] == 1:
                return index

        return -1


print(FirstNotRepeatingchar("mdlsi.nolxdjl8n.fi;oduoi;s"))

while True:
    a=input()
    while '][' in a or '(' in a:
        while '()' in a:
            a=(a.replace('()','[1]'))
        while '(' in a:
            a=(a.replace("(",'['))
            a=(a.replace(')',']'))
        while "][" in a:
            a=(a.replace("][",'],['))
        while '],[' in a:
            a=(a.replace('],[',','))
        while ',1' in a:
            a=(a.replace(',1',''))
        while '1,' in a:
            a = (a.replace('1,', ''))
    print(a.count('['))
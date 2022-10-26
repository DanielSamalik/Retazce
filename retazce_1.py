def uloha1(n:int,ret:str):
    if len(ret)>n:
        return ret[n:n+1:]
    else:
        return "Zly index"


print(uloha1(6,'kamikadze'))
print(uloha1(3,'kuk'))
print(uloha1(0,' '))
print(uloha1(0,''))

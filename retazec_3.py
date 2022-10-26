def uloha3(ret:str):
    sam = "aeiuoy"
    spol = "qwrtpsfgdhjklzxcmvbn"
    index = False
    for i in range(len(ret)):
        if ret[i] in sam and ret[i]!=spol:
            index=True
        else:
            index=False
            break;
    return index
print(uloha3("kukucka"))
print(uloha3("aaaaaauuu"))
print( uloha3("aeioux"))
print(uloha3("o"))
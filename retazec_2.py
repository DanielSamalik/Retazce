def uloha2(ret:str):
    cislice="0123456789"
    cislo=0
    ret2=""
    for i in range(len(ret)):
        if ret[i].isnumeric():
            ret2+=ret[i]
    return len(ret2)
print(uloha2("Na farme mame od roku 2012 12 kráv a 230 oviec."))
print(uloha2("Skutok sa stal."))
print(uloha2("snehulienka a 7 trpazlikov."))
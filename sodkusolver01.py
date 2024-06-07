def hol_kezd(z):
    if 10<=z and 12>=z:
        return (0,0)
    if 13<=z and 15>=z:
        return (0,3)
    if 16<=z and 18>=z:
        return (0,6)
    if 20<=z and 22>=z:
        return (3,0)
    if 23<=z and 25>=z:
        return (3,3)
    if 26<=z and 28>=z:
        return (3,6)
    if 30<=z and 32>=z:
        return (6,0)
    if 33<=z and 35>=z:
        return (6,3)
    if 36<=z and 38>=z:
        return (6,6)
def stillzero():
    x=0
    for sor in tabla:
        if x in sor:
            return True
    return False
tabla=[]
ready=False
with open("try.txt","r", encoding="utf-8") as file:
    for id, line in enumerate(file):
        tabla.append(line.strip().split())
for id1,line in enumerate(tabla):
    for id2, digit in enumerate(line):
        tabla[id1][id2]=int(tabla[id1][id2])
for sor in tabla:
    print(sor)
jo=True
while jo:
    jo=stillzero()
    for oszlopid,sor in enumerate(tabla):
        if oszlopid<3:
            holvanid1=10
        elif oszlopid>5:
            holvanid1=30
        else:
            holvanid1=20
        for sorid,szam in enumerate(sor):
            holvanid2=holvanid1+sorid
            if szam==0:
                minta=[1,2,3,4,5,6,7,8,9]
                #sorcheck
                bye=set(minta) & set(sor)
                minta = [ele for ele in minta if ele not in bye]
                #oszlopcheck
                oszlop=[]
                for x in range(9):
                    oszlop.append(tabla[x][sorid])
                bye=set(minta) & set(oszlop)
                minta = [ele for ele in minta if ele not in bye]      
                #negyzetcheck
                sk=hol_kezd(holvanid2)
                negyzet=[]
                for x in range(3):
                    negyzet.append(tabla[sk[0]+x][sk[1]])
                    negyzet.append(tabla[sk[0]+x][sk[1]+1])
                    negyzet.append(tabla[sk[0]+x][sk[1]+2])
                bye=set(minta) & set(negyzet)
                minta = [ele for ele in minta if ele not in bye]    
                if len(minta)==1:
                    tabla[oszlopid][sorid]=minta[0]
            else:
                continue
print(" ")
for sor in tabla:
    print(sor)
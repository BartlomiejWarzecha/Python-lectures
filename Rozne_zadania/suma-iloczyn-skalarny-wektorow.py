def Wekt(v1,v2):
    suma = []
    iloczyn = []
    licz = 0
    for k in v1:
        suma_cz = v1 [licz] + v2 [licz]
        suma.append(suma_cz)
        iloczyn_cz = v1 [licz] * v2 [licz]
        iloczyn.append(iloczyn_cz)
        licz = licz+1
    return suma, iloczyn
    
w1 = [1,1,900,78**2]
w2 = [1,1,890,900]

print(Wekt(w1,w2))
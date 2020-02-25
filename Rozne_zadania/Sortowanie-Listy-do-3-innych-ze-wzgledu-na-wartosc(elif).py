zest1 = []
zest2 = []
zest3 = []

v1 = 5
v2 = 12

lista = [12,4,1,-900,5600,12,2,4,3,2.1,-740,-1200,3400,4500,3,2,5.5,6.5,8.5]

for element in lista:
    if element <= v1:
        zest1.append(element)
    elif element <= v2:
        zest2.append(element)
    else:
        zest3.append(element)

print(zest1)
print(zest2)
print(zest3)
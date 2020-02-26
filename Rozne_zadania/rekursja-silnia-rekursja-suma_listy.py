# Rekursja
# Silnia
# ? def silnia(n):
# ?     licz = 0
# ?     if n == 1:
# ?         return 1
# ?     licz = licz + 1
# ?     res = n * silnia(n-1)
# ?     return res
# ? m = 4
# ? d = silnia(m)
# ? print('Wartość funkcji silnia dla ',m,'  -  ',d)

#Suma elementów listy
def suma(lista):
    if len(lista) == 1:
        return( lista[0] )
    element = lista[0]
    del lista[0]
    res = element + suma(lista)
    return res
dane = [1,2,3,4,200,210]
somma = sum(dane)
print('Dane = ', dane,' Suma danych = ', somma)

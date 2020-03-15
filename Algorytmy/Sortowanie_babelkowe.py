#! Sortowanie babelkowe

def printList(lista):
    for x in lista:
        print(x, end = ', ')
    print('')

def zamien(a, b):
    temp = a
    a = b
    b = temp

def sortowanie_babelkowe(lista):
    for i in range(len(lista)):
        for j in range((len(lista)-1-i)):
            if lista[j] > lista[j+1]:
                zamien(lista[j], lista[j+1])
        printList(lista)

lista = [9, 12, 7, 1, 6, 8, 10, 120, 2]

printList(lista)

sortowanie_babelkowe(lista)
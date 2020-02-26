# ! Aplikacja obliczjaca procent ukonczenia ksiazki

def Procent_ukonczenia(Ksiazka):

    Strony = int(input('Na ktorej stronie ksiazki jestes?   '))
    ukonczenie = (Strony/Ksiazka) * 100
    print('Za toba juz ',round(ukonczenie, 2),'% ksiazki')

Algorytmy_Ilustrowany_Przewodnik = 219

Procent_ukonczenia(Algorytmy_Ilustrowany_Przewodnik)
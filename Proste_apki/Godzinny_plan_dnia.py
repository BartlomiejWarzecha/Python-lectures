# ! Aplikacja do zarzadzania czasem

Moje_zainteresowania = {}
Studia = {}
Zwiazek = {}

Dni =  5;

ksiazka = Moje_zainteresowania["Ksiazka"] = Dni * 1
cwiczenia = Moje_zainteresowania["cwiczenia"] = Dni * 0.5
medytacja = Moje_zainteresowania["medytacja"] = Dni * 0.5
suma_zainteresowan = ksiazka + cwiczenia + medytacja

Informatyka_studia = Studia["Informatyka_studia"] = Dni * 3;
Matematyka_Jezyk_Agnielski = Studia["Matematyka_Jezyk_Agnielski"] = Dni * 1;
suma_studia = Informatyka_studia + Matematyka_Jezyk_Agnielski

Rozmowy = Zwiazek["Rozmowy"] = Dni * 0.5;
suma_zwiazek = Rozmowy;

Godziny =  Dni * 24;
Sen = Dni * 8;
Praca = Dni * 9;
Wolny_czas = Godziny - (Sen + Praca) 

Zapasowy_czas = Wolny_czas - (suma_zainteresowan + suma_studia + suma_zwiazek)

print('Wolny_czas = ',Wolny_czas)
print('Moje zainteresowania zajmuja ',suma_zainteresowan)
print('ksiazka ', ksiazka)
print('cwiczenia ', cwiczenia)
print('medytacja ', medytacja)

print('Wolny_czas = ',Wolny_czas - suma_zainteresowan)
print('Moje studia zajmuja ', suma_studia)
print('Informatyka na studia ', Informatyka_studia)
print('Matematyka i Jezyk Angielski' , Matematyka_Jezyk_Agnielski)

print('Wolny_czas = ',Wolny_czas - (suma_zainteresowan + suma_studia))
print('Moj zwiazek zajmuje ', suma_zwiazek)
print('Rozmowy' , Rozmowy)
print('Wolny_czas = ',Wolny_czas - (suma_zainteresowan + suma_studia + suma_zwiazek))

print('Kazdego dnia w zapasie pozostaje ', (Zapasowy_czas / Dni) * 60,'min')
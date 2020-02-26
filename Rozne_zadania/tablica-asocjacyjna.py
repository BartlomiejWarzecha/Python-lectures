
#Słownik - Tablica asocjacyjna
osoba = {}
osoba["+48 12 4227492"] = "Krystyna"
osoba["+48 22 6554555"] = "Jan"
osoba["+39 8763655"] = "Andrzej"

#Drukowanie całego słownika
print(osoba)

#Drukowanie wybranej pozycji słownika
Telefon = '+39 8763655'
print(Telefon,' ', osoba["+39 8763655"])

#Odszukanie osoby która ma określony nr telefonu
for telefon in osoba:
    if osoba[telefon]=="+39 8763655":
        print(osoba[telefon], ' ',osoba)
    

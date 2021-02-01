# upotreba recnika tj. mapa

dnevnik = {'Pera' : 3, 'Mira' : 4, 'Deki' : 5}

print(type(dnevnik))
print(dnevnik)

print(dnevnik.keys())
print(dnevnik.values())

print(sorted(dnevnik.keys()))
print(sorted(dnevnik.values()))
#dodajemo Mina sa ocenom 2, i Peri popravljamo ocenu na 5
dnevnik['Mina'] = 2
dnevnik['Pera'] = 5
print(dnevnik)


# dobijam informacije o values 
print(dnevnik.get('Pavle'))
print(dnevnik.get('Mina'))
dnevnik['Sonja'] = 3
if 'Sonja' not in dnevnik.keys():
    dnevnik['Sonja'] = 4
else:
    print(dnevnik['Sonja'])

print("\n")
print(dnevnik)

print(dnevnik.items())
# ispisuje uredjene parove kljuc vrednost

for k in dnevnik.keys():
    print(k, dnevnik[k])
import sys

stanje = 'A'
zavrsno = 'D'

prelaz = {('A', 'b'):'B', ('A', 'c'):'CE',
        ('B', 'b'):'D', ('CE','a'):'CE',
        ('CE', 'b'):'D'}

while True:
    try:
        print("Unesi a ili b ili c\n")
        c = input()
        if(c != 'a' and c != 'b' and c != 'c'):
            sys.exit("Pogresan unos!\n")
    
    except EOFError:
        break;

    if prelaz.get((stanje, c)) is None:
        sys.exit("Greska, rec nije deo jezika")
    stanje = prelaz[(stanje, c)]
    print('\t')



if(stanje == zavrsno):
    print("Uspesno")
else:
    print("Neuspesno")
# (a|c)*bc*
import sys
import re

stanje = 'ABD'
zavrsno = 'CE'
prelaz = {('ABD','a'):'ABD', ('ABD', 'b'):'CE', ('ABD', 'c'):'ABD', ('CE', 'c'):'CE'}

rec = input("Unesite kompletnu rec: ")

for c in rec:
    try:
        if(c!='a' and c!='b' and c!='c'):
            raise ValueError("Los karakter je unet!")
    except ValueError as e:
        sys.exit(e)
    if prelaz.get((stanje, c)) is None:
        sys.exit("Stanje greske, rec se ne nalazi u jeziku!")
    stanje = prelaz[(stanje, c)]
if zavrsno == stanje:
    print("Rec se nalazi u jeziku!")
else:
    print("Rec se ne nalazi u jeziku!")

#(ab|c)*b
import sys
import re

stanje = 'ADE'
zavrsno = 'C'
prelaz = {('ADE','a'):'B', ('ADE', 'b'):'C', ('ADE', 'c'):'ADE', ('B', 'b'):'ADE'}

while True:
    try:
        c = input("Unesite a ili b ili c: ")
        if(c!='a' and c!='b' and c!='c'):
            raise ValueError("Pogresan karakter!")
    except EOFError:
        break;
    except ValueError as e:
        sys.exit(e)
    if prelaz.get((stanje, c)) is None:
        sys.exit("Pogresno stanje, rec se ne nalazi u jeziku!")
    stanje = prelaz[(stanje, c)]
if stanje == zavrsno:
    print("Rec se nalazi u jeziku!")
else:
    print("Rec se ne nalazi u jeziku!")

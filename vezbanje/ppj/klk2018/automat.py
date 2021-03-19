import sys
import re


stanje = 'ABD'
zavrsno = 'E'

prelaz = {('ABD', 'a'):'ABD', ('ABD', 'b'):'C', ('ABD', 'c'):'ABD',
('C','c'):'E', ('E','c'):'E'}


while True:
    try:
        c = input("Unesite a ili b ili c:\n")
        if(c != 'a' and c != 'b' and c != 'c'):
            sys.exit("Alfabet je prekoracen")
    except EOFError:
        break;

    if prelaz.get((stanje,c)) is None:
        print("Rec nije deo jezika")
        sys.exit()
    
    stanje = prelaz[(stanje, c)]
    print("\t" + stanje)

if(stanje == zavrsno):
    print("Rec se nalazi u jeziku")
else:
    print("Rec se ne nalazi u jeziku")




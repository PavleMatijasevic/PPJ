#(a\c)*b+c*
import sys
import re
# ne radi kako treba

stanje = 'AD'
zavrsno = 'C'
zavrsno1 = 'E'

prelaz = {('AD', 'a'):'B', ('AD', 'b'):'C', ('AD', 'c'):'AD',('B', 'a'):'C', ('B','b'):'C', ('B','c'):'AD', ('C','b'):'C', ('C', 'c'):'E', ('E','c'):'E'}


rec = input("Unesite celu rec: ")

for c in rec:
    try:
        if(c!='a' and c!='b' and c!='c'):
            raise ValueError("Unet nedozvoljen karakter!")
    except ValueError as e:
        sys.exit(e)
    if prelaz.get((stanje, c)) is None:
        sys.exit("Stanje greske, rec se ne prihvata!")
    stanje = prelaz[(stanje, c)]
if (zavrsno == stanje or zavrsno1 == stanje): 
    print("Rec se nalazi u jeziku!")
else:
    print("Rec se ne nalazi u jeziku!")

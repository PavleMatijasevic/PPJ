#(a\c)*b+c*
import sys
import re
# ne radi kako treba

stanje = 'AD'
zavrsno = 'CE'

prelaz = {('AD', 'a'):'B', ('AD', 'b'):'CE', ('AD', 'c'):'AD',('B', 'a'):'CE', ('B','b'):'CE', ('B','c'):'AD', ('CE','b'):'CE', ('CE', 'c'):'CE', ('CE','c'):'CE'}


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
if zavrsno == stanje:
    print("Rec se nalazi u jeziku!")
else:
    print("Rec se ne nalazi u jeziku!")

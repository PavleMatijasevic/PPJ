import sys
import re

stanje = 'AD'
zavrsno = 'E'

prelaz = {('AD', 'a'):'B', ('AD', 'b'):'C', ('AD','c'):'AD', ('B', 'a'):'B', ('B', 'b'):'E', ('B', 'c'):'AD', ('C', 'c'):'E'}

while True:
    try:
        c = input("Unesite a, b ili c\n")
        if(c!='a' and c!='b' and c!='c'):
            raise ValueError("Nije unet odgovarajuci karakter!\n")
    except EOFError:
        break;
    except ValueError as e:
        print(e)
        sys.exit()
    if prelaz.get((stanje, c)) is None:
        print("Stanje greske, rec se ne prihvata!\n")
        sys.exit()
    stanje = prelaz[(stanje, c)]
    print("\t", stanje)
    
if(stanje == zavrsno):
    print("Rec se nalazi u jeziku i prihvata se\n")
else:
    print("Rec se ne nalazi u jeziku i ne prihvata se\n")

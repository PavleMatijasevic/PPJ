# (b|ca*)b klk 2019 b grupa
import sys

stanje = 'A'
zavrsno = 'D'

prelaz = {('A', 'b'):'B', ('A', 'c'):'CE',
          ('B', 'b'):'D',
          ('CE','a'):'CE', ('CE', 'b'):'D'}

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
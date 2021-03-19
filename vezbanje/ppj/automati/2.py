#(ab|c)*b klk 2019 a grupa
import sys

stanje = 'ADE'
zavrsno = 'C'

prelaz = {('ADE', 'a'):'B', ('ADE', 'b'):'C', ('ADE','c'):'ADE',
('B', 'b'):'ADE'}

while True:
    try:
        c = input("Unesite a ili b ili c\n")
        if(c != 'a' and c != 'b' and c != 'c'):
            raise ValueError("Nije unet ispravan karakter")
   
    except EOFError:
        break

    except ValueError as e:
        print(e)
        sys.exit()
    
    if prelaz.get((stanje, c)) is None:
	    print("Stanje greske. Rec se ne prihvata")
	    sys.exit()
    
    stanje = prelaz[(stanje, c)]
    print("\t" + stanje)

if(stanje == zavrsno):
    print("Rec se nalazi u jeziku")
else:
    print("Rec se ne nalazi u jeziku")

import sys


stanje = 'ADE'
zavrsno = 'C'

prelaz = {('ADE', 'a'):'B', ('ADE', 'b'):'C', ('ADE', 'c'):'ADE', ('B', 'b'):'ADE'}

while True:
    try:
        c = input("Unesite a ili b ili c\n")
        if(c!='a' and c!='b' and c!='c'):
            raise ValueError("Los unos karaktera!\n")
    except EOFError:
        break
    except ValueError as e:
        print(e)
        sys.exit()
    if prelaz.get((stanje, c)) is None:
        print("Stanje greske! Rec se ne nalazi u jeziku\n")
        sys.exit()
    stanje = prelaz[(stanje, c)]
    
if(stanje == zavrsno):
    print("Rec se nalazi u jeziku!\n")
else:
    print("Rec se ne nalazi u jeziku!\n")

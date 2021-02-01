import sys
import re

stanje = 'AC'
zavrsno = 'E'

prelaz = {('AC', 'a'):'B', ('AC', 'b'):'AC', ('B','a'):'B', ('B', 'b'):'D', ('D','a'):'B', ('D','b'):'E', ('E', 'a'):'B', ('E', 'b'):'AC'}


while True:
    try:
        c = input("Unesite a ili b\n")
        if(c != 'a' and c !='b'):
            raise ValueError("Los unos karaktera!!!")
    except EOFError:
        break;
    
    stanje = prelaz[(stanje, c)]
    print("\t" + stanje)

if stanje == zavrsno:
    print("Rec se nalazi u jeziku!\n")
else:
    print("Rec se ne nalazi u jeziku!\n")

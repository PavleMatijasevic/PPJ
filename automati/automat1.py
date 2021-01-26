# (a|b)*abb

import sys
import re

stanje = 'AC'
zavrsno = 'E'

prelaz = {('AC','a'):'B', ('AC','b'):'AC', ('B', 'a'):'B', ('B', 'b'):'D', ('D','a'):'B', ('D','b'):'E', ('E', 'a'):'B', ('E', 'b'):'AC'}

while True:
    try:
        c = input("Unesite a ili b: ")
        if (c!= 'a' and c!='b'):
            raise ValueError("Los unos! Rec se ne nalazi u jeziku!")
    except EOFError:
        break;
    except ValueError as e:
        sys.exit(e)
    
    if prelaz.get((stanje, c)) is None:
        sys.exit("Pogresno stanje, rec se ne nalazi u jeziku")
    stanje = prelaz[(stanje, c)]
if stanje == zavrsno:
    print("Rec se nalazi u jeziku")
else:
    print("Rec se ne nalazi u jeziku")

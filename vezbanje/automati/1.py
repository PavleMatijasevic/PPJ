import sys
#(a|b)*abb
stanje = 'ADE'
zavrsno = 'E'

prelaz = {('AC', 'a'):'B', ('B', 'a'):'B', ('D', 'a'):'B', ('E', 'a'):'B',
 ('AC', 'b'):'AC', ('B','b'):'D', ('D', 'b'): 'E', ('E', 'b'):'AC'}


while True:
    try:
        c = input("Unesite a ili b\n")
        if(c != 'a' and c != 'b'):
            raise ValueError("Nije uneto ni a ni b")
    except EOFError:
        break
    except ValueError as e:
        print(e)
        sys.exit()

    stanje = prelaz[(stanje, c)]
    print("\t" + stanje)

if stanje == zavrsno:
    print("Rec je iz jezika")
else:
    print("Rec nije iz jezika")

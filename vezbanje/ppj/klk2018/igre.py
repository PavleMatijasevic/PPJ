import sys
import re

try:
    f = open("igre.xml", "r")
    datoteka = f.read()
    f.close()
except IOError:
    sys.exit("Neuspesno otvaranje")

ri = re.compile(r'\s*<igra\s*id="(?P<id>\d+)\s*">'
+r"(?=.*?\s*<naziv>\s*(?P<naziv>[A-Za-z0-9;:\(\) ]+)\s*</naziv>)"
+r"(?=.*?\s*<godina>\s*(?P<godina>\d\d\d\d)\s*</godina>)"
+r"(?=.*?\s*<izdavac>\s*(?P<izdavac>[A-Z0-9][A-Za-z0-9 ]+)\s*</izdavac>)"
+r"(?=.*?\s*<platforme>\s*(?P<platforma>[A-Za-z0-9,:; ]+)\s*</platforme>)"
+r"(?=.*?\s*<ocena>\s*(?P<ocena>\d\.\d?)\s*</ocena>)"
+r'.*?</igra>', re.S)

igre = {}

for m in ri.finditer(datoteka):
    id = int(m.group('id'))
    naziv = m.group('naziv')
    godina = int(m.group('godina'))
    izdavac = m.group('izdavac')
    platforma = m.group('platforma')
    ocena = float(m.group('ocena'))
    igre[id] = [naziv, godina, izdavac, platforma, ocena]


if len(sys.argv) == 2 and sys.argv[1] == '-sve':
    print("to do")
else:
    if len(sys.argv) == 3 and sys.argv[1] == '-info':
        naziv = sys.argv[2]
        for v in igre.values():
            if re.search(r''+naziv,v[0],re.I) is not None:
                print(v[0], "(",v[4], ")")
    elif len(sys.argv) == 3 and sys.argv[1] == '-i':
        naziv = sys.argv[2]
        for k, v in igre.items():
            if(naziv == v[2]):
                print(v[0], "(",v[1],")")
    elif len(sys.argv) == 3 and sys.argv[1] == '-p':
        naziv = sys.argv[2]
        for k, v in igre.items():
            if naziv in v[3]:
                print(v[0])
    else:
        print("Los unos!")

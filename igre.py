import sys
import re

try:
    f = open("igre.xml", "r")
    datoteka = f.read()
    f.close()
except IOError:
    sys.exit("Losa datoteka")
    
ri = re.compile(r'\s*<igra\s*id="(?P<id>\d+)\s*">'
+r"(?=.*?\s*<naziv>(?P<naziv>[A-Za-z:;,'\d ]+)\s*</naziv>)"
+r"(?=.*?\s*<godina>(?P<godina>\d\d\d\d)\s*</godina>)"
+r"(?=.*?\s*<izdavac>(?P<izdavac>[A-Za-z0-9 ]+)\s*</izdavac>)"
+r"(?=.*?\s*<platforme>(?P<platforme>[A-Za-z0-9,;: ]+)\s*</platforme>)"
+r"(?=.*?\s*<ocena>(?P<ocena>\d(\.\d)?)\s*</ocena>)"
+r'.*?\s*</igra>',re.S)
    
igre = {}

for m in ri.finditer(datoteka):
    id = int(m.group('id'))
    naziv = m.group('naziv')
    godina = int(m.group('godina'))
    izdavac = m.group('izdavac')
    platforme = m.group('platforme')
    ocena = float(m.group('ocena'))
    igre[id] = [naziv, godina, izdavac, platforme, ocena]
    
if len(sys.argv) == 2 and sys.argv[1] == '-sve':
    for v in sorted(igre.values()):
        print(v[0])
elif len(sys.argv) == 3 and sys.argv[1] == '-info':
        rec = sys.argv[2]
        for v in igre.values():
            if re.search(r''+rec, v[0], re.I) is not None:
                print(v[0], "(", v[4], ")")
elif len(sys.argv) == 3 and sys.argv[1] == '-i':
    naziv_iz = sys.argv[2]
    for k, v in igre.items():
        if(naziv_iz == v[2]):
            print(v[0], "(",v[1],")")
elif len(sys.argv) == 3 and sys.argv[1] == '-p':
    naziv_pl = sys.argv[2]
    for v in igre.values():
        if re.search(r''+naziv_pl, v[3], re.I):
            print(v[0])
            




















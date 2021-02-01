import sys
import re
#ne radi kako treba
f = sys.argv[1]
if(re.match(r"^.*\.csv$", sys.argv[1]) == None):
    sys.exit(sys.argv[1]+" nije dobar format")
try:
    fajl = open(f, "r")
    datoteka = fajl.read()
    fajl.close()
except IOError:
    sys.exit("Neuspesno otvaranje")

ri = re.compile(r"(?P<ime>[A-Z][a-z]+\s*([A-Za-z]+)?\s*([A-Z][a-z]+)?),"
+r"(?P<drzava>\s*[A-Z][a-z]+),"
+r"(?P<broj_golova>\s*\d+),"
+r"(?P<broj_utakmica>\s*\d+),"
+r"(?P<karijera>\s*\d\d\d\d-(\d\d\d\d)?),"
+r"(?P<klubovi>\s*([A-Z][A-Za-z0-9, ]+)+)"
)    



igraci = {}

for m in ri.finditer(datoteka):
    ime = m.group('ime')
    drzava = m.group('drzava')
    broj_golova = int(m.group('broj_golova'))
    broj_utakmica = int(m.group('broj_utakmica'))
    karijera = m.group('karijera')
    klubovi = m.group('klubovi')
    igraci[ime] = [drzava, broj_golova, broj_utakmica, karijera, klubovi]

if len(sys.argv) == 3 and sys.argv[2] == '-g':
    for k, v in igraci.items():
        prosek = v[1]/v[2]
        print(k, prosek)
else:
    if len(sys.argv) == 4 and sys.argv[2] == '-t':
        klub = sys.argv[3:]
        print(klub)
        for v in igraci.values():
            if re.match(r''+klub,v[3], re.I) is not None:
                print(v[0])
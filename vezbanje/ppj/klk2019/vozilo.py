import sys
import re

try:
    with open("vozilo.xml", "r") as f:
        datoteka = f.read()
except IOError:
    sys.exit("Otvaranje datoteke")

ri = re.compile(r'<vozilo\s*id="\s*(?P<id>[0-9]+)\s*">'
+r"(?=.*?\s*<fabrika>\s*(?P<fabrika>[A-Za-z-:; ]+)\s*</fabrika>)"
+r"(?=.*?\s*<model>\s*(?P<model>[A-Za-z0-9-:;' ]+)\s*</model>)"
+r"(?=.*?\s*<godina>\s*(?P<godina>\d{4})\s*</godina>)"
+r"(?=.*?\s*<cena>\s*(?P<cena>\d+)\s*</cena>)"
+r"(?=.*?\s*<snaga_motora>\s*(?P<snaga_motora>\d+)\s*</snaga_motora>)"
+r"(?=.*?\s*<zapremina>\s*(?P<zapremina>\d+)\s*</zapremina>)"
+r"(?=.*?\s*<gorivo>\s*(?P<gorivo>(Benzin|Dizel|TNG)-(EURO3|EURO4|EURO5|EURO6))\s*</gorivo>)"
+r'.*?</vozilo>', re.S)

automobili = {}

for m in ri.finditer(datoteka):
    id = int(m.group('id'))
    fabrika = m.group('fabrika')
    model = m.group('model')
    god = int(m.group('godina'))
    cena = int(m.group('cena'))
    snaga = int(m.group('snaga_motora'))
    zapremina = float(m.group('zapremina'))
    gorivo = m.group('gorivo')
    automobili[id] = [fabrika, model, god, cena, snaga, zapremina, gorivo]

if len(sys.argv) < 2:
    for k, v in automobili.items():
        print(v[2], v[0], v[1], v[5], v[4], v[6], v[3])
else:
    if sys.argv[1] == "-f" and len(sys.argv) == 3:
        fab = sys.argv[2]
        for k, v in automobili.items():
            if(v[0] == fab):
                print(v[2], v[0], v[1], v[5], v[4], v[6], v[3])
    elif sys.argv[1] == "-c" and len(sys.argv) == 4:
        cmin= int(sys.argv[2])
        cmax = int(sys.argv[3])
        for k, v in automobili.items():
            if(v[3]>=cmin and v[3]<= cmax):
                print(v[2], v[0], v[1], v[5], v[4], v[6], v[3])
    elif sys.argv[1] == "-z" and len(sys.argv) == 4:
        zmin = float(sys.argv[2])
        zmax = float(sys.argv[3])
        for k, v in automobili.items():
            if(v[5]>= zmin and zmax>= v[5]):
                print(v[2], v[0], v[1], v[5], v[4], v[6], v[3])
    elif sys.argv[1] == "-g" and len(sys.argv) == 4:
        gorivo = sys.argv[2]
        norma = sys.argv[3]
        s = gorivo + "-" + norma
        for k, v in automobili.items():
            if(v[6] == s):
                print(v[2], v[0], v[1], v[5], v[4], v[6], v[3])
    else:
        print("Greska prijatelju!")

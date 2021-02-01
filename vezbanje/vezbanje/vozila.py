import sys
import re

try:
    f = open("vozila.xml", "r")
    datoteka = f.read()
    f.close()
except IOError:
    sys.exit("Argumenti")


ri = re.compile(r'<vozilo\s*id="\s*(?P<id>[0-9]+)\s*">'
+r"(?=.*?\s*<fabrika>\s*(?P<fabrika>[A-Za-z-:; ]+)\s*</fabrika>)"
+r"(?=.*?\s*<model>\s*(?P<model>[A-Za-z0-9-:;' ]+)\s*</model>)"
+r"(?=.*?\s*<godina>\s*(?P<godina>\d{4})\s*</godina>)"
+r"(?=.*?\s*<cena>\s*(?P<cena>\d+)\s*</cena>)"
+r"(?=.*?\s*<snaga_motora>\s*(?P<snaga>\d+)\s*</snaga_motora>)"
+r"(?=.*?\s*<zapremina>\s*(?P<zapremina>\d+)\s*</zapremina>)"
+r"(?=.*?\s*<gorivo>\s*(?P<gorivo>(Benzin|Dizel|TNG)-(EURO3|EURO4|EURO5|EURO6))\s*</gorivo>)"
+r'.*?</vozilo>', re.S)

vozila = {}

for m in ri.finditer(datoteka):
    id = int(m.group('id'))
    fabrika = m.group('fabrika')
    model = m.group('model')
    godina = int(m.group('godina'))
    cena = int(m.group('cena'))
    snaga = int(m.group('snaga'))
    zapremina = float(m.group('zapremina'))
    gorivo = m.group('gorivo')
    vozila[id] = [fabrika, model, godina, cena, snaga, zapremina, gorivo]



if(len(sys.argv) < 2):
    for k, v in vozila.items():
        print(v[0], v[1], v[2], v[3], v[4], v[5], v[6])
else:
    if(len(sys.argv) == 3 and sys.argv[1] == "-f"):
        fab = sys.argv[2]
        for k, v in vozila.items():
            #print(fab, v[0], '\n')
            if(fab == v[0]):
                print(v[2], v[0],v[1],v[5],v[4],v[6],v[3])
    elif len(sys.argv) == 4 and sys.argv[1] == "-c":
        cmin = int(sys.argv[2])
        cmax = int(sys.argv[3])
        for k, v in vozila.items():
            if(cmin <= v[3] and cmax >= v[3]):
                print(v[2], v[0],v[1],v[5],v[4],v[6],v[3])
    elif len(sys.argv) == 4 and sys.argv[1] == "-z":
        zmin = int(sys.argv[2])
        zmax = int(sys.argv[3])
        for k, v in vozila.items():
            if(zmin <= v[5] and zmax >= v[5]):
                print(v[2], v[0],v[1],v[5],v[4],v[6],v[3])
    elif len(sys.argv) == 4 and sys.argv[1] == "-g":
        gor = sys.argv[2]
        norma = sys.argv[3]
        sve = gor + "-" + norma
        for k, v in vozila.items():
            if(sve == v[6]):
                print(v[2], v[0],v[1],v[5],v[4],v[6],v[3])
    else:
        print("Neka greska prijatelju")

                

import sys
import re


try:
    f = open("televizori.xml", "r")
    datoteka = f.read()
    f.close()
except IOError:
    sys.exit("Ucitavanje datoteke je problem!")

ri = re.compile(r'\s*<televizor\s*id="(?P<id>\d)\s*">'
+r"(?=.*?\s*<rmarka>\s*(?P<marka>[A-Za-z0-9 ]+)\s*</rmarka>)"
+r"(?=.*?\s*<model>(?P<model>[A-Za-z0-9;:, ]+)\s*</model>)"
+r"(?=.*?\s*<godina>(?P<godina>\d\d\d\d)\s*</godina>)"
+r"(?=.*?\s*<diag>(?P<dijagonala>\d\d?)\s*</diag>)"
+r"(?=.*?\s*<kolicina>(?P<kolicina>\d+)\s*</kolicina>)"
+r"(?=.*?\s*<panel>(?P<panel>(TN|IPS|VA|LED)-(HD|FHD|UHD))\s*</panel>)"
+r"(?=.*?\s*<cena>(?P<cena>\d+)\s*</cena>)"
+r'.*?</televizor>', re.S)

tv = {}

for m in ri.finditer(datoteka):
    id = int(m.group('id'))
    marka = m.group('marka')
    model = m.group('model')
    godina = int(m.group('godina'))
    dijagonala = float(m.group('dijagonala'))
    kolicina = int(m.group('kolicina'))
    panel = m.group('panel')
    cena = int(m.group('cena'))
    tv[id] = [marka, model, godina, dijagonala, kolicina, panel, cena]


if len(sys.argv) == 3 and sys.argv[1] == "-r":
    trazena_marka = sys.argv[2]
    for k, v in tv.items():
        if(trazena_marka == v[0]):
            print(v[2], v[0], v[1], v[3], v[5], v[6], v[4])
elif len(sys.argv) == 4 and sys.argv[1] == "-c":
        min = int(sys.argv[2])
        max = int(sys.argv[3])
        for k, v in tv.items():
            if(v[6]>=min and v[6]<=max):
                print(v[2], v[0], v[1], v[3], v[5], v[6], v[4])
elif len(sys.argv) == 4 and sys.argv[1] == "-d":
    min = int(sys.argv[2])
    max = int(sys.argv[3])
    for k, v in tv.items():
        if(v[3]>=min and v[3]<=max):
            print(v[2], v[0], v[1], v[3], v[5], v[6], v[4])
elif len(sys.argv) == 3 and sys.argv[1] == "-g":
    godina = int(sys.argv[2])
    for k, v in tv.items():
        if(godina == v[2]):
            print(v[2], v[0], v[1], v[3], v[5], v[6], v[4])
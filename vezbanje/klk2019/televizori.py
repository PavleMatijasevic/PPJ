import sys
import re

try:
    with open("televizori.xml") as f:
        datoteka = f.read()
except IOError:
    sys.exit("Otvaranje")

ri = re.compile(r'<televizor\s*id="(?P<rbr>[1-9])\s*">'
+r"(?=.*?\s*<rmarka>\s*(?P<rmarka>[A-Za-z ]+)\s*</rmarka>)"
+r"(?=.*?\s*<model>\s*(?P<model>[A-Za-z0-9 ]+)\s*</model>)"
+r"(?=.*?\s*<godina>\s*(?P<godina>\d{4})\s*</godina>)"
+r"(?=.*?\s*<diag>\s*(?P<diag>\d\d)\s*</diag>)"
+r"(?=.*?\s*<kolicina>\s*(?P<kolicina>[0-9]*)\s*</kolicina>)"
+r"(?=.*?\s*<cena>\s*(?P<cena>[0-9]+)\s*</cena>)"
+r"(?=.*?\s*<panel>\s*(?P<panel>(TN|IPS|VA|LED)-(HD|FHD|UHD))\s*</panel>)"
+r'.*?</televizor>', re.S)

televizori = {}

for m in ri.finditer(datoteka):
    rbr = m.group('rbr')
    marka = m.group('rmarka')
    model = m.group('model')
    godina = int(m.group('godina'))
    diag = float(m.group('diag'))
    kolicina = int(m.group('kolicina'))
    panel = m.group('panel')
    cena = int(m.group('cena'))
    televizori[rbr] = [marka, model, godina, diag, panel, cena, kolicina]


if len(sys.argv) < 2:
    for k, v in televizori.items():
        print(v)
else:
    if sys.argv[1] == "-r" and len(sys.argv) == 3:
        rmarka = sys.argv[2]
        for k, v in televizori.items():
            if(v[0] == rmarka):
                print(v[2]," ",v[0]," ",v[1]," ",v[3],"in ",v[5],"din: ",v[6]," komada na stanju")
    elif sys.argv[1] == "-c" and len(sys.argv)  == 4:
        cmin = int(sys.argv[2])
        cmax = int(sys.argv[3])
        for k, v in televizori.items():
            if(v[5]>cmin and v[5]<cmax):
                print(v[2]," ",v[0]," ",v[1]," ",v[3],"in ",v[5],"din: ",v[6]," komada na stanju")
    elif sys.argv[1] == "-d" and len(sys.argv) == 4:
        mind = int(sys.argv[2])
        maxd = int(sys.argv[3])
        for k, v in televizori.items():
            if(v[3]>=mind and v[3]<=maxd):
                print(v[2]," ",v[0]," ",v[1]," ",v[3],"in ",v[5],"din: ",v[6]," komada na stanju")
    elif sys.argv[1] == "-g" and len(sys.argv) == 3:
        god = int(sys.argv[2])
        for k, v in televizori.items():
            if(v[2] == god):
               print(v[2]," ",v[0]," ",v[1]," ",v[3],"in ",v[5],"din: ",v[6]," komada na stanju")
    else:
        sys.exit("Greska prijatelju!")
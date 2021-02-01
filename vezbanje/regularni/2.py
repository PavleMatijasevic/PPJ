import re
import sys
import os

def obradi_datoteku(ime_datoteke):
    if(ime_datoteke in obradjene_datoteke):
        return
    obradjene_datoteke.append(ime_datoteke)

try:
    with open(ime_datoteke, "r") as f:
        datoteka = f.read()
except IOError:
    sys.exit("Otvaranje")

regex = re.compile(r'\b<a\s+href\s*=\s*(.*?)>.*?</a>', re.I | re.S)


for m in regex.finditer(datoteka):
    url = m.group(1)
    obradi_datoteku(url)

if len(sys.argv) > 1:
    pocetna = sys.argv[1]
else:
    pocetna = "index.html"

obradjene_datoteke = []
obradi_datoteku(pocetna)

for datoteka in obradjene_datoteke:
    print(datoteka)
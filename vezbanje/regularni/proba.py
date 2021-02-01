import sys
import re

try:
    f = open("knjige.xml", "r")
    datoteka = f.read()
    f.close()
except IOError:
    sys.exit("Neuspesno otvaranje knjige.xml")

if len(sys.argv) < 2:
    sys.exit("Ulazni Argumenti")

autor = False
godina = False
izdavac = False
cena = False

naslov = None

if re.match(r'-[agic]+', sys.argv[1]):
    if 'a' in sys.argv[1]:
        autor = True
    if 'g' in sys.argv[1]:
        godina = True
    if 'i' in sys.argv[1]:
        izdavac = True
    if 'c' in sys.argv[1]:
        cena = True
    
if len(sys.argv) > 2:
    naslov = sys.argv[2]
else:
    sys.exit("Naslov knjige")

ri = re.compile(r"<knjiga\s*rbr\s*=\s*'.'>"
+r"\s*<naslov>\s*(?P<ime_knjige>[A-Za-z ]+)\s*</naslov>"
+r"\s*<autor>\s*(?P<autor>[A-Za-z ]+)\s*</autor>"
+r"\s*<godina_izdavanja>\s*(?P<godina_izdavanja>\d\d\d\d)\s*</godina_izdavanja>"
+r"\s*<izdavac>(?P<izdavac>.*)\s*</izdavac>"
+r"\s*<cena valuta='[rsd|eur]'\s*>(?P<cena>[\d|\d\d|\d\d\d|\d\d\d\d])\s*</cena>"
+r"\s*</knjiga>",re.S)

katalog = {}

for m in ri.finditer(datoteka):
    katalog[m.group('rbr')] = [m.group('naslov'), m.group('autor'), 
    m.group('izdavac'), m.group('godina'), m.group('cena'), m.group('valuta')]

podaci = None

for k,v in katalog.items():
    if v[0] == naslov:
        podaci = v[1:]
        break

if autor:
    print("Autor:", podaci[0])
if izdavac:
    print("Izdavac:", podaci[1])
if godina:
    print("Godina izdanja:", podaci[2])
if cena:
    print("Cena: ", podaci[3], podaci[4])

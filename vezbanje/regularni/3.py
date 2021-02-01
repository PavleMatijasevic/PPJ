import re
import sys

try:
    f = open(sys.argv[1], "r")
    datoteka = f.read()
    f.close()
except IOError:
    sys.exit("Argumenti")

ri = re.compile(r"<tr>"
+r"\s*<td>\s*(?P<ime>[A-Za-z ]+)\s*</td>"
+r"\s*<td>\s*(?P<prakticni>0|[1-9]\d|100)\s*</td>"
+r"\s*<td>\s*(?P<usmeni>0|[1-9]\d|100)\s*</td>"
+r"\s*</tr>")

studenti = []
poeni = []

for m in ri.finditer(datoteka):
    ime_prezime = m.group('ime')
    ukupnoPoena = int(m.group('prakticni')) + int(m.group('usmeni'))
    ukupnoPoena /= 2
    studenti.append(ime_prezime)
    poeni.append(ukupnoPoena)

konacnaLista = list(zip(poeni, studenti))

konacnaLista.sort(reverse=True)
try:
    f = open("rezultati.txt", "w")
except IOError:
    sys.exit("Problem otvaranje rezultati.txt datoteke")

for j ,(bodovi, imena) in enumerate (konacnaLista):
    f.write(str(j+1) + "." + imena + " : " + str(bodovi) + "\n")
  


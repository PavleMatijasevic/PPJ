import sys
import re

if len(sys.argv) != 2:
    sys.exit("Argumenti")
if re.match(r"^.+\.html$", sys.argv[1], re.I) is None:
    print("Pogresna html ekstenzija")
else:
    print("Dobra ekstenzija")


try:
    f = open(sys.argv[1], "r")
    data = f.read()
    f.close()
except IOError:
    sys.exit()

ri = re.compile(r"<tr>"
+ r"\s*<td>\s*(?P<ime>[A-Z][a-z]+(\s+[A-Z][a-z]+)+)\s*</td>"
+ r"\s*<td>\s*(?P<prakticni>\d|[1-9]\d|100)\s*</td>"
+ r"\s*<td>\s*(?P<usmeni>\d|[1-9]\d|100)\s*</td>"
+ r"\s*</tr>", re.S);
	


studenti = []
poeni = []

for m in ri.finditer(data):
    student = m.group("ime")
    prakticni = int(m.group("prakticni"))
    usmeni = int(m.group("usmeni"))
    studenti.append(student)
    poeni.append(prakticni+usmeni)

parovi = sorted(zip(poeni, studenti))
parovi.reverse()
for s,p in parovi:
    print(s, p)
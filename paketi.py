import sys
import re

try:
    f = open("paketi.xml", "r")
    datoteka = f.read()
    f.close()
except IOError:
    exit("Losa datoteka!")

ri = re.compile(r'\s*.*?\s*<paket\s*id="(?P<id>\d)">'
+r"(?=.*?\s*<naziv>\s*(?P<naziv>[A-Za-z]+)\s*</naziv>)"
+r"(?=.*?\s*<verzija>\s*(?P<verzija>\d+\.\d+\.\d+)\s*</verzija>)"
+r"(?=.*?\s*<opis>\s*(?P<opis>[A-Za-z0-9,\. ]+)\s*</opis>)"
+r"(?=.*?\s*<repo>(?P<repo>(github|gitlab|bitbucket))\s*</repo>)"
+r"(?=.*?\s*<veb>\s*(?P<veb>(www\.)?[a-zA-Z\.]+(\.org|\.com))\s*</veb>)"
+r'.*?\s*</paket>',re.S)

paket = {}
for m in ri.finditer(datoteka):
    id = int(m.group('id'))
    naziv = m.group('naziv')
    verzija = m.group('verzija')
    opis = m.group('opis')
    repo = m.group('repo')
    veb = m.group('veb')
    paket[id] = [naziv, verzija, opis, repo, veb]
    
if len(sys.argv) == 2 and sys.argv[1] == '-a':
    for  v in sorted(paket.values()):
        print("[",v[0],"]",'v',v[1], v[3], v[4], v[2])
elif len(sys.argv) == 3 and sys.argv[1] == '-v':
    naziv_p = sys.argv[2]
    for v in paket.values():
        if(naziv_p == v[0]):
            print("Verzija: ", v[1])
elif len(sys.argv) == 3 and sys.argv[1] == '-w':
    naziv_p = sys.argv[2]
    for v in paket.values():
        if(naziv_p == v[0]):
            print("Veb:", v[4])
elif len(sys.argv) == 3 and sys.argv[1] == '-r':
    naziv_p = sys.argv[2]
    for v in paket.values():
        if(naziv_p == v[0]):
            print("Repozitorijum:", v[3])
elif len(sys.argv) == 3 and sys.argv[1] == '-o':
    naziv_p = sys.argv[2]
    for v in paket.values():
        if(naziv_p == v[0]):
            print("Opis: ", v[2])


 
  

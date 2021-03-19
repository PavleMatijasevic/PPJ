import sys
import re

try:
    f = open("paketi.xml","r")
    datoteka = f.read()
    f.close()
except IOError:
    sys.exit("Lose ucitavanje fajla")
               
#ri = re.compile(r'\s*<paket\s*id="(?P<id>\d+)\s*">'
#+r"(?=.*?\s*<naziv>\s*(?P<naziv>[A-Za-z])\s*</naziv>)"
#+r"(?=.*?\s*<verzija>\s*(?P<verzija>\d\.\d\.\d)\s*</verzija>)"
#+r"(?=.*?\s*<opis>\s*(?P<opis>[A-Za-z. ]+)\s*</opis>)"
#+r"(?=.*?\s*<repo>(?P<repo>(github|gitlab|bitbucket))\s*</repo>)"
#+r"(?=.*?\s*<veb>(?P<veb>(www.)?[A-Za-z.]+(com|org))\s*</veb>)"
#+r'.*?</paket>', re.S)

ri = re.compile(r'\s*<paket\s*id="(?P<id>\d+)\s*">'
+r"(?=.*?\s*<naziv>(?P<naziv>[A-Za-z]+)\s*</naziv>)"
+r"(?=.*?\s*<verzija>(?P<verzija>\d+\.\d+(\.\d+)?)\s*</verzija>)"
+r"(?=.*?\s*<opis>\s*(?P<opis>[A-Za-z,:;\. ]+)\s*</opis>)"
+r"(?=.*?\s*<repo>\s*(?P<repo>(github|gitlab|bitbucket))\s*</repo>)"
+r"(?=.*?\s*<veb>\s*(?P<veb>(www.)?[A-Za-z0-9\.]+(com|org))\s*</veb>)"
+r'.*?</paket>', re.S)



pak = {}

for m in ri.finditer(datoteka):
    id = m.group('id')
    naziv = m.group('naziv')
    verzija = m.group('verzija')
    opis = m.group('opis')
    repo = m.group('repo')
    veb = m.group('veb')
    pak[id] = [naziv, verzija, opis, repo, veb]

#print(pak)

if len(sys.argv) == 2 and sys.argv[1] == '-a':
    print("to do?")
else:
    if len(sys.argv) == 3 and sys.argv[1] == '-v':
        naziv = sys.argv[2]
        for k, v in pak.items():
            if(naziv == v[0]):
                print(v[1])
    elif len(sys.argv) == 3 and sys.argv[1] == '-w':
        naziv = sys.argv[2]
        for k, v in pak.items():
            if(naziv == v[0]):
                print(v[4])
    elif len(sys.argv) == 3 and sys.argv[1] == '-r':
        naziv = sys.argv[2]
        for k, v in pak.items():
            if(naziv == v[0]):
                print(v[3])
    elif len(sys.argv) == 3 and sys.argv[1] == '-o':
        naziv = sys.argv[2]
        for k, v in pak.items():
            if(naziv == v[0]):
                print(v[2])
    else:
        sys.exit("Lose unosenje argumenata")
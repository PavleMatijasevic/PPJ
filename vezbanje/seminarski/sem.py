import sys
import os
import re

if len(sys.argv) < 2:
	sys.exit("Argumenti")
	
homedir = sys.argv[1]

studenti = {} # mapa kljuc -> indeks, vrednost->ime

putanja = os.path.join(homedir, "indeksi");
try:
	with open(putanja, "r") as f:
		for linija in f.readlines():
			if (linija[-1] == '\n'): 
				linija = linija[:-1] # posmatram liniju bez prelaska na novi red
			m = re.match(r'^((m[mnvrlia]|a[aif])([01]\d|20)(00[1-9]|0[1-9]\d|[1-5]\d\d)),\s*([A-Za-z ]+)$', linija)
			if m is not None:
				info = re.split(r',\s*', linija)
				studenti[info[0]] = info[1]
except IOError:
    sys.exit("Open")

# print(studenti)

re_dir = re.compile(r'^((m[mnvrlia]|a[aif])([01]\d|20)(00[1-9]|0[1-9]\d|[1-5]\d\d))$'); # ovo su imena 4 direktorijuma data u alas formatu
re_file = re.compile(r'^(\d)\.(java|c|cpp|pas)$', re.I)

max_br_zad = 0
zadaci = {} # mapa

# kljuc -> (indeks, red_br_zad)
# vrednost -> ekstenzija

for f in os.listdir(homedir):       # listdir prolazi kroz sve pod direktorijume homedir-a i to je f(mi18123...)
	stud_dir = os.path.join(homedir, f);       # stud_dir su putanje do svakog stud. direktorijuma
	m = re_dir.match(f)     # ako ne postoji m onda je None
	if os.path.isdir(stud_dir) and m is not None and f in studenti:
		indeks = m.group(1)
		for sf in os.listdir(stud_dir):
			zadatak = os.path.join(stud_dir, sf)
			m = re_file.match(sf)
			if os.path.isfile(zadatak) and m is not None:
				zad = int(m.group(1))
				zadaci[(indeks, zad)] = m.group(2)
				if zad > max_br_zad:
					max_br_zad = zad
					
for indeks, ime in studenti.items():
	print("\nIme: " + ime)
	for i in range(1, max_br_zad):
		if (indeks,i) in zadaci:
			print("\t" + str(i) + "." + zadaci[(indeks, i)])
		else:
			print("\t" + str(i) + ".-")


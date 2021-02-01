import sys
# citam iz datoteke ulaz.txt i prepisujem u datoteku izlaz.txt
if len(sys.argv) != 3:
    sys.exit("Problem su argumenti")

try:
    f = open(sys.argv[1], "r")
except IOError:
    sys.exit("Problem je u ulaznoj datoteci")
    
sadrzaj = f.read()
f.close()

try:
    f = open(sys.argv[2], "w")
except IOError:
    sys.exit("Problem je u izlaznoj datoteci")

f.write(sadrzaj)
f.close()
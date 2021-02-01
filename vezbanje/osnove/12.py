import sys
# prepisuje iz jedne u drugu datoteku ali liniju po liniju
if len(sys.argv) != 3:
    sys.exit("Problem je u argumentima komandne linije")

try:
    f = open(sys.argv[1], "r")
    sadrzaj = f.readlines()
except IOError:
    sys.argv("Problem je u ulaznoj datoteci")

f.close()

try:
    f = open(sys.argv[2], "w")
except IOError:
    sys.exit("Problem u izlaznoj datoteci")

for i in range(0, len(sadrzaj)):
    f.write(str(i+1) + " : " + sadrzaj[i])
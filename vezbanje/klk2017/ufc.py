import sys
import re

f = sys.argv[1]
if(re.match(r"^.*\.csv$", f) == None):
    sys.exit(sys.argv[1]+" nije dobar format")
try:
    fajl = open(f, "r")
    datoteka = fajl.read()
    fajl.close()
except IOError:
    sys.exit("Neuspesno otvaranje")


ri = re.compile(r"(?P<event_date>\d\d?/\d\d?/\d\d\d\d);"
+r"(?P<f1name>[A-Za-z ]+);"
+r"(?P<f2name>[A-Za-z ]+);"
+r"(?P<f1result>(win|loss));"
+r"(?P<f2result>(win|loss));"
+r"(?P<method>(Submission|Decision|KO));"
+r"(?P<ref>[A-Za-z ]+);"
+r"(?P<round>[1|2|3|4|5]);"
+r"(?P<time>(\d\d?:\d\d?))"
, re.S)

borac = {}
id = 0
for m in ri.finditer(datoteka):
    event_date = m.group('event_date')
    f1name = m.group('f1name')
    f2name = m.group('f2name')
    f1result = m.group('f1result')
    f2result = m.group('f2result')
    method = m.group('method')
    ref = m.group('ref')
    runda = int(m.group('round'))
    time = m.group('time')
    borac[id] = [event_date, f1name, f2name, f1result, f2result, method, ref, runda, time]
    id += 1

if len(sys.argv) == 3 and sys.argv[2] == "-b":
    print("ulaz")
else:
    if len(sys.argv) == 4 and sys.argv[2] == "-m":
        metod = sys.argv[3]
        for k, v in borac.items():
            if(metod == v[5]):
                if(v[3] == "win"):
                    print(v[1])
                else:
                    print(v[2])
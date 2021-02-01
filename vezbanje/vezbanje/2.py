import sys
import re

try:
    f = open("vozila.xml", "r")
    datoteka = f.read();
    f.close();

except IOError:
    sys.exit("Ulazna datoteka je problem!")

ri = re.compile(r'(?=.*?<vozilo\s*id="(?P<id>\d)\s*">)'
+r"(?=.*?\s*<fabrika>\s*(?P<fabrika>[A-Za-z-;: ]+)\s*</fabrika>)"                
+r"(?=.*?\s*<model>\s*(?P<model>[A-Za-z0-9-:;' ]+)\s*</model>)"
+r"(?=.*?\s*<godina>\s*(?P<godina>\d\d\d\d)\s*</godina>)"
+r"(?=.*?\s*<zapremina>\s*(?P<zapremina>\d+(\.\d)?)\s*</zapremina>)"
+r"(?=.*?\s*<gorivo>\s*(?P<gorivo>(Benzin|Dizel|TNG)-(EURO3|EURO4|EURO5|EURO6)\s*)</gorivo>)"
+r"(?=.*?\s*<cena>\s*(?P<cena>\d+)\s*</cena>)"
+r"(?=.*?\s*<snaga_motora>\s*(?P<snaga>\d+)\s*</snaga_motora>)"
+r'.*?</vozilo>', re.S)


auto = {}

for m in ri.finditer(datoteka):
    id = int(m.group('id'))
    fabrika = m.group('fabrika')
    model = m.group('model')
    godina = int(m.group('godina'))
    zapremina = float(m.group('zapremina'))
    gorivo = m.group('gorivo')
    cena = int(m.group('cena'))
    snaga_motora = int(m.group('snaga'))
    auto[id] = [fabrika, model, godina, zapremina, gorivo,
                cena, snaga_motora]
    
if len(sys.argv) == 3 and sys.argv[1] == '-f':
    fabrika = sys.argv[2]
    for k, v in auto.items():
        if(fabrika == v[0]):
            print(v[2]," ",v[0]," ",v[3],"cm3 ",v[6],"kW ",v[4]," ",v[5],"evra")
            
elif len(sys.argv) == 4 and sys.argv[1] == '-c':
    maxi = int(sys.argv[3])
    mini = int(sys.argv[2])
    for k, v in auto.items():
        if(v[5] >= mini and v[5] <= maxi):
            print(v[2]," ",v[0]," ",v[3],"cm3 ",v[6],"kW ",v[4]," ",v[5],"evra")
elif len(sys.argv) == 4 and sys.argv[1] == '-z':
    maxi = int(sys.argv[3])
    mini = int(sys.argv[2])
    for k, v in auto.items():
        if(v[3] >= mini and v[3] <= maxi):
            print(v[2]," ",v[0]," ",v[3],"cm3 ",v[6],"kW ",v[4]," ",v[5],"evra")
elif len(sys.argv) == 4 and sys.argv[1] == '-g':
    gorivo = sys.argv[2]
    norma = sys.argv[3]
    zajedno = gorivo+"-"+norma
    for k, v in auto.items():
        if(zajedno == v[4]):
            print(v[2]," ",v[0]," ",v[3],"cm3 ",v[6],"kW ",v[4]," ",v[5],"evra")
else:
    print("Niste uneli odgovarajuci argument! Vise srece drugi put!!!")
    
            
    
    
    
    
    
    
    
    
    
    
    
    
    
    

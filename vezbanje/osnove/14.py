import sys
import re

poruka = "Danas je sreda"
poruka2 = "Sutra je nova godina"
poruka3 = "ova poruka pocinje malim slovom a zavrsava se velikiM"
poklapanje = re.match("[A-Z][a-z]+",poruka)

if poklapanje is not None:
    print("Pronadjeno je poklapanje : " + " ' " + poklapanje.group() + " ' "+ " u poruci: " + poruka)
else:
    print("Nema poklapanja u poruci: " + poruka)


poklapanje = re.match("[A-Z][a-z0-9 ]+" , poruka2)

if poklapanje is not None:
    print("Pronadjeno je poklapanje : " + " ' "+ poklapanje.group() + " ' " +  " u poruci: " + poruka2)
else:
    print("Nema poklapanja u poruci: " + poruka2)

poklapanje = re.match("[A-Z][a-z0-9 ]+" , poruka3)
if poklapanje is not None:
    print("Pronadjeno je poklapanje : " + " ' " +  poklapanje.group() + " ' "  +  " u poruci: " + poruka3)
else:
   print("Nema poklapanja u poruci: " + poruka3)

print(poruka.replace("Danas", "Sutra"))
print(poruka)
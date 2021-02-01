# malo slovo koje je samoglasnik menjam velikim slovom, ako nije slovo -, ostalo ostaje isto
a = "Moze i ovako."
b = ""
print(a)

for x in a:
    if x.lower and x in('a', 'e', 'i', 'o', 'u'):
        b = b + x.upper()
    elif not x.isalpha():
        b = b + '-'
    else:
        b = b + x
print(b)

# ispisujem sve stepene broja 2 od 0 do 10

e = 2
pocetak = 0
kraj = 10
####### 1. nacin ##########
while pocetak < kraj:
    print(e ** pocetak)
    pocetak = pocetak + 1
###########################

##### 2. nacin###############

for i in range(0, 11, 1):
    print(2, " ^ " , i ,  " = " , 2**i)
###########################


######### stampanje svakog elementa liste u novom redu ####
l = ["Pavle", "Matijasevic", "programiranje", "ggmu", "lista", "element"]

for i in l:
    print(i)

m = len(l)
for k in range(0, m, 1):
    print(l[k])
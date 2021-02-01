a = [1, 2, 3, 4, 5]
print(a)
print(type(a))
L = list((2, 4, 6 ,8, 10))
l = list(a)
print(L)
print(l)

lista2 = ['paja', "pavle", 12, 15, "acab"]
print(lista2)

lista3 = ["pavle", "ppj", "kuzma", 1234, 124.42]
print(lista3)

print(lista2 + lista3)

b = lista2
print(b) # b je isto sto je i lista2

b = b * 3 # nadovezivanje nad samim sobom
c = ["pako", 123, "alkas", 'paja', 1245]

print(b)
a.append(6)
print(a)
print(c)

if 'paja' in c:
    c.remove('paja')
else:
    print("Ne nalazi se u nizu ")
print(c)


if 3 in a:
    print("broj 3 se nalazi u a")
else:
    print("Broj 3 se ne nalazi u a")

a = [1, 2, 3, 4, 5]
a.pop()
print(a)

a.reverse()
print(a)
a.sort(reverse=False)
print(a)

stringovi = ["Pavle", "Mina", "Zika", "Perica", "Matijasevic"]
stringovi.sort(key=len, reverse=True)
print(stringovi)
stringovi.sort(key=len, reverse=False)
print(stringovi)
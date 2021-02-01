s = ["Pavle", "Mina", "Matijasevic", "ppj", "python"]
b = set(s)
a = set("Magija")
print(set(s))
print(a)

if 'f' not in a:
    a.add('f')
else:
    a.remove('f')
print(a)

a = set("Magija")
b = set("Mudro")

print("\n",a,"\n",b)
#presek
print(a&b)
#unija
print(a|b)
#razlika
print(a-b)
#simetricna razlika
print(a^b)
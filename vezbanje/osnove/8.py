x = int(input("Unesite jedan broj : "))
y = int(input("Unesite drugi broj : "))

def zbir(n, k):
    return n + k

print("Zbir brojeva ", x, " i " , y, " je: ", zbir(x, y))

def proizvod(n, k):
    return n * k

print("Proizvod brojeva ", x, " i ", y, " je: ", proizvod(x, y))

def paran(n):
    if(n % 2 == 0):
        return 1
    else:
        return 0

if(paran(x)):
    print("Broj", x, "je paran")
else:
    print("Broj", x, "nije paran")

if(paran(y)):
    print("Broj", y, "je paran")
else:
    print("Broj", y, "nije paran")


if(paran(zbir(x, y))):
    print("Broj", zbir(x, y), "je paran")
else:
    print("Broj", zbir(x, y), "nije paran")

def pozitivan(n):
    if(n>0):
        return 1
    else:
        return 0

if(pozitivan(x)):
    print("Broj", x, "je pozitivan")
else:
    print("Broj", x, "nije pozitivan")

def kvadrat_broja(n):
    return n*n

def prost(n):
    brojac = 1
    for i in range(2, n-1, 1):
        if(n % i == 0):
            brojac = brojac + 1
    if(brojac == 1):
        print("je prost")    
    else:
        print("nije prost")



print("Broj", x)
prost(x)
print("Broj", y)
prost(y)
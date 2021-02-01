# fibonacijevi brojevi => 0 1 1 2 3 5 8 13

def fibonaci(x):
    niz = []
    a = 0
    b = 1
    niz.append(a)
    niz.append(b)
    niz.append(a+b)

    a = b
    for i in range(2, x+1, 1):
        niz.append(a+b)         
        x = b
        b = b + a
        a = x                  
            
    
    return niz


n = int(input("Uneti broj n: "))

print(fibonaci(n))
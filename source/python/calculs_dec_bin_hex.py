def mystere(a,b,base=10):
    if base == 10:
        return int(a+b)
    elif base == 2:
        return bin(a+b)
    else:
        return hex(a+b)

def somme(a,b,base=10):
    if base == 10:
        return int(a+b)
    elif base == 2:
        return bin(a+b)
    else:
        return hex(a+b)
    
def produit(a,b,base=10):
    if base == 10:
        return int(a*b)
    elif base == 2:
        return bin(a*b)
    else:
        return hex(a*b)

print("--- Somme ---")
print(somme(14,29))
print(somme(14,29,2))
print(somme(14,29,16))
print("--- Produit ---")
print(produit(14,29))
print(produit(14,29,2))
print(produit(14,29,16))
print("--- Carré ---")
print(produit(somme(14,29),somme(14,29)))
print(produit(somme(14,29),somme(14,29),2))
print(produit(somme(14,29),somme(14,29),16))
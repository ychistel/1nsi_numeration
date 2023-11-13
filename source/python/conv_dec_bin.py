n = int(input("nombre décimal à convertir:"))

while n > 0:
    r = n % 2
    n = n // 2
    print(r)

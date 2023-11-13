n = int(input("nombre décimal à convertir:"))

while n > 0:
    r = n % 16
    n = n // 16
    if r < 10:
        print(r)
    elif r == 10:
        print('A')
    elif r == 11:
        print('B')
    elif r == 12:
        print('C')
    elif r == 13:
        print('D')
    elif r == 14:
        print('E')
    else:
        print('F')
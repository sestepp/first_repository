
liczba1 = int(input('Wprowadź liczbę 1: '))
liczba2 = int(input('Wprowadź liczbę 2: '))

liczby_w_zakresie = []

i = liczba1
while i <= liczba2:
    liczby_w_zakresie.append(i)
    i += 1

suma = 0
sześć_liczb = []

if (liczba2 - liczba1 + 1) > 20:
    for i in liczby_w_zakresie:
        suma += liczby_w_zakresie[i-1]
    średnia = suma / len(liczby_w_zakresie)
    a = średnia // 1
    b = średnia // 1
    for i in range(3):
        a -= 1
        b += 1
        sześć_liczb.append(a)
        sześć_liczb.append(b)
    print(sześć_liczb)

else:
    for i in liczby_w_zakresie:
        print(i)
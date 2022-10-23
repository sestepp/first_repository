liczba1 = float(input('Wprowadź liczbę 1: '))
liczba2 = float(input('Wprowadź liczbę 2: '))

# Funkcja zawierająca działania
def działania():
    print('Wynik dodawania: ', liczba1 + liczba2)
    print('Wynik odejmowania: ', liczba1 - liczba2)
    print('Wynik mnożenia: ', liczba1 * liczba2)
    if liczba1 * liczba2 == 10:
        print('Yay!')
    print('Wynik dzielenia: ', liczba1 / liczba2)
    print('Wynik kwadratu liczby 1: ', liczba1 ** 2)
    print('Wynik kwadratu liczby 2: ', liczba2 ** 2)
    print('Wynik pierwiastka kwadratowego liczby 1: ', liczba1 ** (1/2))
    print('Wynik pierwiastka kwadratowego liczby 2: ', liczba2 ** (1/2))
try:
    # Warunek, żeby obie liczby były większe od zera
    if liczba1 < 0 and liczba2 < 0:
        print('Wartość obu liczb jest mniejsza od zera')
    
    # Pierwiastek z kwadratu liczby - zamienia liczbę ujemną na dodatnią
    elif liczba1 < 0 or liczba2 < 0:
        liczba1 = (liczba1 ** 2) ** (1/2)
        liczba2 = (liczba2 ** 2) ** (1/2)
        działania()

    else:
        działania()

except:
    print('Próba wykonania dzielenia przez 0')

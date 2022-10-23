from random import randint as losowanie
koniec = None
while koniec != 'N':
    liczba1 = float(input('Wprowadź liczbę 1: '))
    liczba2 = float(input('Wprowadź liczbę 2: '))
    
    symbol = input('Wybierz symbol:\n Dodawanie: +\n Odejmowanie: -\n Mnożenie: *\n Dzielenie: /\n Potęgowanie: #\n Pierwiastkowanie: ^\n Losowanie liczby: x\n Symbol ' )
    
    if symbol == '+':
        print(liczba1 + liczba2)
    elif symbol == '-':
        print(liczba1 - liczba2)
    elif symbol == '*':
        print(liczba1 * liczba2)
    elif symbol == '/':
        print(liczba1 / liczba2)
    elif symbol == '#':
        print(liczba1 ** liczba2)
    elif symbol == '^':
        print(liczba1 ** (1/liczba2))
    elif symbol == 'x':
        min = float(input('Wprowadź dolną wartość: '))
        max = float(input('Wprowadź górną wartość: '))
        print('Wylosowania liczba:', losowanie(min, max))

    koniec = input('Czy chcesz wprowadzić nowe dane? (T/N)\n')
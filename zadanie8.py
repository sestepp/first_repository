liczba = int(input('Wprowadź liczbę: '))
choinka = []
j = 1
k = liczba - 1
for i in range(liczba):
    if j == 1:
        choinka.append(' '*(k +1))
        choinka.append('X')
        print(''.join(choinka))
        choinka.clear()
        j += 2
    elif int(i/2) != (i/2):
        choinka.append(' '*k)
        choinka.append('*'*(j//3-1))
        choinka.append('o')
        choinka.append('*'*(j-j//3))
        print(''.join(choinka))
        choinka.clear()
        j += 2
        k -= 1
    elif int(i/2) == (i/2):
        choinka.append(' '*k)
        choinka.append('*'*(j-j//2))
        choinka.append('o')
        choinka.append('*'*(j//2-1))
        print(''.join(choinka))
        choinka.clear()
        j += 2
        k -= 1

choinka.append(' '*(liczba))
choinka.append('U')
print(''.join(choinka))
choinka.clear()
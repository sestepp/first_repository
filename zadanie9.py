tranzakcje = []
nadany = input('Nadaj pin: ')
def PIN():
  pin = input('Wprowadź PIN: ')
  if pin == nadany:
    return
  else:
    PIN()

wybór = None

while wybór != '0':
  print('Co chcesz zrobić w kolejnym kroku?\n0 Koniec\n1 Wpłata\n2 Wypłata\n3 Saldo')
  wybór = input('Wybierz opcje ')
  if wybór == '1':
    PIN()
    kwota = input('Wpłacana kwota: ')
    tranzakcje.append(int(kwota))
    saldo = sum(tranzakcje)
  elif wybór == '2':
    PIN()
    kwota = float(input('Wypłacana kwota: '))
    if kwota > saldo:
      print('Nie masz dość środków na koncie')
    else:
      tranzakcje.append(-float((kwota)))
      saldo = sum(tranzakcje)
  elif wybór == '3':
    PIN()
    saldo = sum(tranzakcje)
    print(saldo)

  saldo = sum(tranzakcje)
  print(tranzakcje)  

   


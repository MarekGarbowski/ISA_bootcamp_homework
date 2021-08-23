
while True:
    print(30 * '-')
    print('   Wybierz opcję z menu:')
    print('1. Oblicz średnią arytmetyczną')
    print('2. Podnieś do potęgi')
    print('3. Porównaj liczby')
    print('4. Wyjście z programu')
    print(30 * '*')

    decision = input('Podaj swój wybór: ')
    if decision == '1':
        print('Oblicz średnią arytmetyczną')
        digit_1 = int(input('Podaj pierwszą liczbę: '))
        digit_2 = int(input('Podaj drugą liczbę: '))
        result = (digit_1 + digit_2) / 2
        print(30 * '_')
        print('Srednia arytmetyczna podanych liczb wynosi: {} '.format(result))
    if decision == '2':
        print('2. Podnieś do potęgi')
        digit_1 = int(input('Podaj pierwszą liczbę: '))
        digit_2 = int(input('Podaj drugą liczbę: '))
        result = digit_1 ** digit_2
        print(30 * '_')
        print('Wynik potęgi liczby pierwszej do drugiej wynosi: {}'.format(result))
    if decision == '3':
        print('3. Porównaj liczby')
        digit_1 = int(input('Podaj pierwszą liczbę do prównania: '))
        digit_2 = int(input('Podaj drugą liczbę do porównania: '))
        if digit_1 > digit_2:
            print(30 * '_')
            print('Liczba {} jest większa od {}'.format(digit_1, digit_2))
        else:
            print(30 * '_')
            print('Liczba {} jest mniejsza od {}'.format(digit_1, digit_2))
    if decision == '4':
        print('Koniec programu.')
        break

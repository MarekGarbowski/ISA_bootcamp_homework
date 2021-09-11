
# 1). Stwórz funkcję nazwaną dodajListy() która zwróci nową listę sumując ze sobą elementy
# na tych samych indeksach  .
# Możesz przypuścić, że jako parametry do funkcji podawane są zawsze listy zawierające
# tylko liczby. Jeżeli listy są różnej długości, funkcja powinna wyświetlić napis
# ‘Podane listy muszą być tej samej długości’.


def add_lists(a, b):
    c = []
    if len(a) == len(b):
        for x, y in zip(a, b):
            c.append(x + y)
        return c
    else:
        return 'Podane listy muszą być tej samej długości'


if __name__ == "__main__":
    choice = 't'
    while choice == 't':
        list_1 = []
        list_2 = []
        list_length_1 = int(input('Podaj jaką długą pierwszą listę chcesz stworzyć: '))
        for item in range(list_length_1):
            digit = int(input('Podaj liczbę do listy: '))
            list_1.append(digit)
        list_length_2 = int(input('Podaj jaką długą drugą listę chcesz stworzyć: '))
        for item in range(list_length_2):
            digit = int(input('Podaj liczbę do listy: '))
            list_2.append(digit)
        print('Suma pozycji obu list wynosi:', add_lists(list_1, list_2))
        choice = input('Jeśl chcesz jesze raz wykonać sumowanie, wpisz "t", jeśli nie to wciśnij dowolny klawisz:  ')

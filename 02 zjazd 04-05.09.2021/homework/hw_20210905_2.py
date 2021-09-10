import math


# 2). Stwórz funkcję nazwaną zbadajTrojkat() która przyjmie jako argumenty długości
# boków trójkąta. Funkcja powinna zwrócić, czy trójkąt jest prostokątny,
# równoramienny, równoboczny, różnoboczny lub nieprawidłowy.


def check_triangle(a, b, c):
    while is_valid_triangle(a, b, c):
        if c == math.sqrt(a ** 2 + b ** 2) or b == math.sqrt(a ** 2 + c ** 2) or a == math.sqrt(b ** 2 + c ** 2):
            return 'Podany trójkąt jest prostokątny.'
        elif a == b or a == c or b == c:
            return 'Podany trójąt jest równoramienny.'
        elif a == b == c:
            return 'Podany trójkąt jest równoboczny.'
        else:
            return 'Podany trójkąt jest różnoboczy.'
    return 'Trójkąt nie jest parwidłowy'


def is_valid_triangle(a, b, c):
    if a + b > c and b + c > a and c + a > b:
        return True
    else:
        return False


if __name__ == "__main__":
    choice = 't'
    while choice == 't':
        x = int(input('Podaj bok A trójkąta "ABC": '))
        y = int(input('Podaj bok B trójkąta "ABC": '))
        z = int(input('Podaj bok C trójkąta "ABC": '))
        print(check_triangle(x, y, z))
        choice = input('Jeśli chcessz jeszcze raz sprawdzić trójkąt wcisnij "t", jeśli nie to dowolny inny: ')


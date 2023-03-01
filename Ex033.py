primeiro = int(input("Diga o primeiro valor: "))
segundo = int(input("Diga o segundo valor: "))
terceiro = int(input("Diga o terceiro valor: "))

if primeiro > segundo and primeiro > terceiro:
    print("O maior numero eh o {}" .format(primeiro))
elif segundo > primeiro and segundo > terceiro:
    print("O maior numero eh o {}" .format(segundo))
else:
    print("O maior numero eh o {}" .format(terceiro))

if primeiro < segundo and primeiro < terceiro:
    print("O menor numero eh o {}" .format(primeiro))
elif segundo < primeiro and segundo < terceiro:
    print("O menor numero eh o {}" .format(segundo))
else:
    print("O menor numero eh o {}" .format(terceiro))
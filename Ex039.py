ano = int(input("Diga o ano de nascimento: "))
idade = 2023 - ano
tempo1 = 18 - idade
tempo2 = idade - 18

if idade < 18:
    print("Você ainda vai se alistar no serviço militar, faltam {} anos.".format(tempo1))
elif idade == 18:
    print("Você deve se alistar esse ano no serviço militar.")
else:
    print("Ja passou do tempo do alistamento, passaram {} anos.".format(tempo2))

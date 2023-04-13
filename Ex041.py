ano = int(input("Diga o ano de nascimento do atleta: "))
idade = 2023 - ano

if idade <= 9:
    print("A categoria eh mirim.")
elif idade > 9 and idade < 14:
    print("A categoria eh infantil.")
elif idade >= 14 and idade < 19:
    print("A categoria eh infantil.")
elif idade >= 19 and idade < 20:
    print("A categoria eh infantil.")
else:
    print("A categoria eh master.")
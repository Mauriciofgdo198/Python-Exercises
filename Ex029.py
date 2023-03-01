velocidade = int(input("Qual a velocidade(km/h) do carro agora? "))
multa = (velocidade - 80) * 7
if velocidade <= 80:
    print("Você esta abaixo do limite, continue dirigindo com segurança!")
else:
    print("Você esta acima do limite, sua multa sera no valor de: {} reais" .format(multa))
sexo = str(input("Digite o sexo(M/F) da pessoa: ")).strip().upper()[0]
while sexo not in "FfMm":
    sexo = str(input("Dados invalidos, digite novamente: ")).strip().upper()[0]
print("Sexo {} registrado com sucesso!".format(sexo))

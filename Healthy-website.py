sexo = str(input('Qual seu sexo? (Masculino ou feminino) '))
sexo = sexo.upper()
sexo = sexo[0]
idade = float(input('Qual sua idade? (Caso tenha menos de 1 ano escreva 0.3 para 3 meses) '))
peso = float(input('Qual seu peso(kg)? '))
altura = float(input('Qual seu altura(m)? '))
tmb = float(input("Quantas vezes você faz exercicios na semana? "))


#Agua ------------------------------------------------------------------------------------------------------------------
agua = 35 * peso
print('O seu consumo de água ideal é de {} ml'.format(agua))


#Indice de massa corporal ----------------------------------------------------------------------------------------------
imc = peso / altura**2
print('O seu IMC é de {:0.2f}'.format(imc))


#Sono (Tempo que a pessoa deve dormir) ---------------------------------------------------------------------------------
if idade < 1:
    print("O bebe deve dormir de 12 a 17 horas por dia. ")
elif idade >= 1 and idade < 3:
    print("A criança deve dormir de 11 a 14 horas por dia. ")
elif idade >= 3 and idade < 6:
    print("A criança deve dormir de 10 a 13 horas por dia. ")
elif idade >= 6 and idade < 14:
    print("A criança deve dormir de 9 a 11 horas por dia. ")
elif idade >= 14 and idade < 17:
    print("A jovem deve dormir 10 horas por dia. ")
elif idade >= 18 and idade < 65:
    print("Os adultos devem dormir 7 a 9 horas por dia. ")
else:
    print("Os idosos devem dormir 7 a 8 horas por dia. ")


#Taxas de atividade (TMB)-----------------------------------------------------------------------------------------------
#Sedentários (pouco ou nenhum exercício) fator = 1.2
if tmb < 1:
    print("Voce eh sedentario, geralmente pratica pouco ou nenhum exercicio. ")
#Levemente ativo (exercício leve 1 a 3 dias por semana) fator = 1.375
elif tmb >= 1 and tmb < 3:
    print("Voce eh levemente ativo, geralmente pratica de 1 a 3 dias de exercicios por semana. ")
#Moderadamente ativo (exercício moderado, faz esportes 3 a 5 dias por semana) fator = 1.55
elif tmb >= 3 and tmb < 5:
    print("Voce eh moderadamente ativo, geralmente pratica de 3 a 5 dias de exercicios por semana. ")
#Altamente ativo (exercício pesado de 5 a 6 dias por semana) fator = 1.725
elif tmb >= 5 and tmb <= 6:
    print("Voce eh altamente ativo, geralmente pratica de 5 a 6 dias de exercicios por semana. ")
#Extremamente ativo (exercício pesado diariamente e até 2 vezes por dia) fator = 1.9
else:
    print("Voce eh extremamente ativo, geralmente pratica exercicios diarios durante toda a semana. ")


#caloriahomens = fator da taxa de atividade * {66+[(13.7*peso +(5*altura*100) – (6.8*idade)]}---------------------------
calculo = float(66 + ((13.7 * peso + (5 * altura * 100) - (6.8 * idade))))
if sexo == "M":
#Sedentários (csm) (pouco ou nenhum exercício) fator = 1.2
    if tmb < 1:
        csm = (1.2 * calculo)
        print("A quantidade de caloria que um homem sedentario consome eh em torno de {}" .format(csm))
#Levemente ativo (lsm) (exercício leve 1 a 3 dias por semana) fator = 1.375
    elif tmb >= 1 and tmb < 3:
        lsm = (1.375 * calculo)
        print("A quantidade de caloria que um homem levemente ativo consome eh em torno de {}" .format(lsm))
#Moderadamente ativo (msm) (exercício moderado, faz esportes 3 a 5 dias por semana) fator = 1.55
    elif tmb >= 3 and tmb < 5:
        msm = (1.55 * calculo)
        print("A quantidade de caloria que um homem moderadamente ativo consome eh em torno de {}" .format(msm))
#Altamente ativo (asm) (exercício pesado de 5 a 6 dias por semana) fator = 1.725
    elif tmb >= 5 and tmb <= 6:
        asm = (1.725 * calculo)
        print("A quantidade de caloria que um homem altamente ativo consome eh em torno de {}" .format(asm))
#Extremamente ativo (esm) (exercício pesado diariamente e até 2 vezes por dia) fator = 1.9
    else:
        esm = (1.9 * calculo)
        print("A quantidade de caloria que um homem extremamente ativo consome eh em torno de {}" .format(esm))


#caloriamulheres = fator da taxa de atividade * {655+[(9.6*peso +(1.8*altura*100) – (4.7*idade)]}-----------------------
calculofem = float(655+((9.6 * peso +(1.8 * altura * 100) - (4.7 * idade))))
if sexo == "F":
#Sedentários (csf) (pouco ou nenhum exercício) fator = 1.2
    if tmb < 1:
        csf = (1.2 * calculofem)
        print("A quantidade de caloria que uma mulher sedentaria consome eh em torno de {}" .format(csf))
#Levemente ativo (lsf) (exercício leve 1 a 3 dias por semana) fator = 1.375
    elif tmb >= 1 and tmb < 3:
        lsf = (1.375 * calculofem)
        print("A quantidade de caloria que uma mulher levemente ativa consome eh em torno de {}" .format(lsf))
#Moderadamente ativo (msf) (exercício moderado, faz esportes 3 a 5 dias por semana) fator = 1.55
    elif tmb >= 3 and tmb < 5:
        msf = (1.55 * calculofem)
        print("A quantidade de caloria que uma mulher moderadamente ativa consome eh em torno de {}" .format(msf))
#Altamente ativo (asf) (exercício pesado de 5 a 6 dias por semana) fator = 1.725
    elif tmb >= 5 and tmb <= 6:
        asf = (1.725 * calculofem)
        print("A quantidade de caloria que uma mulher altamente ativa consome eh em torno de {}" .format(asf))
#Extremamente ativo (esf) (exercício pesado diariamente e até 2 vezes por dia) fator = 1.9
    else:
        esf = (1.9 * calculofem)
        print("A quantidade de caloria que uma mulher extremamente ativa consome eh em torno de {}" .format(esf))


#Carboidratos 55%-------------------------------------------------------------------------------------------------------
carboidrato = 0.55
#Gordura 25%------------------------------------------------------------------------------------------------------------
gordura = 0.25
#Proteina 20%-----------------------------------------------------------------------------------------------------------
proteina = 0.2


#Masculino (Carboidrato, proteina e gordura)----------------------------------------------------------------------------
if sexo == "M":
#Sedentários (csm) (pouco ou nenhum exercício)
    if tmb < 1:
        ccsm = carboidrato * csm
        pcsm = proteina * csm
        gcsm = gordura * csm
        print("Você deve consumir {:0.2f} calorias de carboidrato, {} calorias de proteina e {} calorias de gordura. ". format(ccsm, pcsm, gcsm))
#Levemente ativo (lsm) (exercício leve 1 a 3 dias por semana)
    elif tmb >= 1 and tmb < 3:
        clsm = carboidrato * lsm
        plsm = proteina * lsm
        glsm = gordura * lsm
        print("Você deve consumir {:0.2f} calorias de carboidrato, {:0.2f} calorias de proteina e {:0.2f} calorias de gordura. ". format(clsm, plsm, glsm))
#Moderadamente ativo (msm) (exercício moderado, faz esportes 3 a 5 dias por semana)
    elif tmb >= 3 and tmb < 5:
        cmsm = carboidrato * msm
        pmsm = proteina * msm
        gmsm = gordura * msm
        print("Você deve consumir {:0.2f} calorias de carboidrato, {:0.2f} calorias de proteina e {:0.2f} calorias de gordura. ". format(cmsm, pmsm, gmsm))
#Altamente ativo (asm) (exercício pesado de 5 a 6 dias por semana)
    elif tmb >= 5 and tmb <= 6:
        casm = carboidrato * asm
        pasm = proteina * asm
        gasm = gordura * asm
        print("Você deve consumir {:0.2f} calorias de carboidrato, {:0.2f} calorias de proteina e {:0.2f} calorias de gordura. ". format(casm, pasm, gasm))
#Extremamente ativo (esm) (exercício pesado diariamente e até 2 vezes por dia)
    else:
        cesm = carboidrato * esm
        pesm = proteina * esm
        gesm = gordura * esm
        print("Você deve consumir {:0.2f} calorias de carboidrato, {:0.2f} calorias de proteina e {:0.2f} calorias de gordura. ". format(cesm, pesm, gesm))

#Feminino (Carboidrato, proteina e gordura)-----------------------------------------------------------------------------
if sexo == "F":
#Sedentários (csf) (pouco ou nenhum exercício)
    if tmb < 1:
        ccsf = carboidrato * csf
        pcsf = proteina * csf
        gcsf = gordura * csf
        print("Você deve consumir {:0.2f} calorias de carboidrato, {} calorias de proteina e {} calorias de gordura. ". format(ccsf, pcsf, gcsf))
#Levemente ativo (lsf) (exercício leve 1 a 3 dias por semana)
    elif tmb >= 1 and tmb < 3:
        clsf = carboidrato * lsf
        plsf = proteina * lsf
        glsf = gordura * lsf
        print("Você deve consumir {:0.2f} calorias de carboidrato, {:0.2f} calorias de proteina e {:0.2f} calorias de gordura. ". format(clsf, plsf, glsf))
#Moderadamente ativo (msf) (exercício moderado, faz esportes 3 a 5 dias por semana)
    elif tmb >= 3 and tmb < 5:
        cmsf = carboidrato * msf
        pmsf = proteina * msf
        gmsf = gordura * msf
        print("Você deve consumir {:0.2f} calorias de carboidrato, {:0.2f} calorias de proteina e {:0.2f} calorias de gordura. ". format(cmsf, pmsf, gmsf))
#Altamente ativo (asf) (exercício pesado de 5 a 6 dias por semana)
    elif tmb >= 5 and tmb <= 6:
        casf = carboidrato * asf
        pasf = proteina * asf
        gasf = gordura * asf
        print("Você deve consumir {:0.2f} calorias de carboidrato, {:0.2f} calorias de proteina e {:0.2f} calorias de gordura. ". format(casf, pasf, gasf))
#Extremamente ativo (esf) (exercício pesado diariamente e até 2 vezes por dia)
    else:
        cesf = carboidrato * esf
        pesf = proteina * esf
        gesf = gordura * esf
        print("Você deve consumir {:0.2f} calorias de carboidrato, {:0.2f} calorias de proteina e {:0.2f} calorias de gordura. ". format(cesf, pesf, gesf))
import random
a1 = str(input('Qual o nome do primeiro aluno? '))
a2 = str(input('Qual o nome do segundo aluno? '))
a3 = str(input('Qual o nome do terceiro aluno? '))
a4 = str(input('Qual o nome do quarto aluno? '))
lista = [a1, a2, a3, a4]
h1 = random.choice(lista)
print('Dentre os alunos {}, {}, {} e {}. O escolhido para apagar o quadro sera: {}'.format(a1, a2, a3, a4, h1))
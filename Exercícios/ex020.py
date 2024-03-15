from random import shuffle

a1 = str(input('primeiro Aluno: '))
a2 = str(input('Segundo Aluno: '))
a3 = str(input('Terceiro Aluno: '))
a4 = str(input('quarto Aluno: '))

lista = [a1, a2, a3, a4]
# Não Precisa de Variável
shuffle(lista)

print(lista)

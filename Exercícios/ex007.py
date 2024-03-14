nome = str(input('Qual é o nome do Aluno? '))

n1 = float(input('Qual é a nota da primeira prova? '))
n2 = float(input('Qual a nota da segunda prova? '))

m = (n1 + n2) / 2

print('\nA Nota do Aluno {}, referente às Provas:\n'
      'Prova 1: {}\n'
      'Prova 2: {}\n\n'
      'A Nota final do Aluno {} é {}'.format(nome, n1, n2, nome, m))

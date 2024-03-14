# + Adição
# - Subtração
# * Multiplicação, funciona com str ('Oi'*5)
# / Divisão
# ** Potência >> pow(n1, n2) >> raiz (1/n)
# // Divisão inteira
# % Resto da divisão

# Ordem
# 1° ()
# 2° **
# 3° * / // %
# 4° + -

nome = input('Qual é o seu nome? ')
# É possivel inserir modificadores nesse espaço
# :> (Alinhamento à Direita)
# :< (Alinhamento à Esquerda)
# :^ (Centralizado)
# :*^ (Espaço preenchido com o "*")
# :-^20 (Quantidade de Espaços)
print('Prazer {:-^20}!'.format(nome))

n1 = int(input('Digite o Primeiro número: '))
n2 = int(input('Digite o Segundo número: '))
a = n1 + n2
s = n1 - n2
m = n1 * n2
d = n1 / n2
d1 = n1 // n2
r = n1 % n2
p = n1 ** n2
rz = n1 ** (1/n2)
# É possível determinar casas decimais usando ":.'n'"
# É possível terminar a linha comalgo basta usar ", end=' '"
print('soma {},\nsubtração {}\nmultiplicação {}\n'
      'divisão {:.2}\ndivisão inteira {}\nresto {}\n'
      'portência {}\nraiz {:.2}'.format(a, s, m, d, d1, r, p, rz)
      )
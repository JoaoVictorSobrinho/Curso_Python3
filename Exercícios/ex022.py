"""f = str(input('Qual é o nome do fiscal? '))
d1 = (input('Qual é a data da viagem? '))
d2 = int(input('Quantos dias de viagem? '))
r = (input('Qual é a rota? '))

s = f.upper().split()
s1 = s[0][0]
s2 = s[1][0]
s3 = s[2][0]
sigla = s1+s2+s3

d = d1.split()
di = d[0][:2]
m = d[2][:3]
df = int(di)
print('\n\n{}_{}_{}_{}_{}'.format(sigla, m.upper(), di, df+d2, r.upper()))"""

# Exercício dia 19 de março
# strip serve pra tirar os espaços
nome = str(input('Qual o seu nome completo? ')).strip()

print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))
# Count serve para subitrair espaços da frase
print('Seu nome tem {} Letras!'.format(len(nome)-nome.count(' ')))
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
separa = nome.split()
print('Seu primeiro nome é {} e tem {} letras'.format(separa[0], len(separa[0])))

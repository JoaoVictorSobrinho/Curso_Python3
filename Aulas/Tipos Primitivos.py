# Tipos Primitivos
# int - Inteiros - {4, 2, 3, -7}
# float - Reais - {4.5, 5.78, -7.0}
# bool - Verdadeiro ou Falso - {True, False}
# str - Letras - {'Olá', '7.5', ''}

n1 = (input('Digite um número inteiro '))
# Type retorna o tipo do input
print(type(n1))
# .isnumeric retorna se é possível ou não converter str para int ou float (True e False)
print('Numero? ',n1.isnumeric())
# .isalpha se é alfabético
print('Alfabético? ',n1.isalpha())
# .isalnum se é alfanumérico
print( 'Alfanumérico? ',n1.isalnum())
n2: float = float(input('Digite um número Real '))
print(type(n2))
n3 = bool(input('Você é um funcionário?  '))
print(type(n3))
n4 = str(input('Qual o seu nome '))
print(type(n4))

s = n1 + n2

print('Você digitou o númeor {}'.format(n1))
print('Você digitou o númeor {}'.format(n2))
print('A soma dos valores {} e {}: {}'.format(n1, n2, s))
print('Sua resposta foi {}'.format(n3))
print('Seu nome é {}'.format(n4))

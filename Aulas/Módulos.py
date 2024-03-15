# Módulos são adicições ao Python > import <
# É pssóvel adicionar toda uma biblioteca:
# import PACOTE
# Ou importar apenas um item dessa biblioteca
# from PACOTE import ITEM
import math
import emoji

print(emoji.emojize('Olá, Mundo!:thumbsup:'))
print(emoji.emojize('Olá, mundo :innocent:'))

num = int(input('Digite um numero: '))
raiz = math.sqrt(num)
print('A raiz desse número é: {}'.format(math.ceil(raiz)))

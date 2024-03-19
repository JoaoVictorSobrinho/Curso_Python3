frase = str(input('Escreva uma frase: ')).lower().strip()
print('Primeira A posição {}'.format(frase.find('a') + 1))
print('Ultima A posição {}'.format(frase.rfind('a') + 1))
print('Quantidade de A é: {}'.format(frase.count('a')))

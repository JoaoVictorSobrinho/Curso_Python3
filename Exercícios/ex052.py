number = int(input('Digite um número: '))
total = 0
# número primo é divisível por 1 e ele mesmo
# Não é divisivel por nenhum número maior que ele
for c in range(1, (number + 1)):
    if number % c == 0:
        print('\033[33m', end=' ')
        total += 1
        if total >= 2:
            break
    else:
        print('\033[31m', end=' ')
    print('{}'.format(c), end=' ')
print('\033[m')
"""if total == 2:
    print('\nPRIMO')
    
else:
    print('\nNÃO PRIMO')"""

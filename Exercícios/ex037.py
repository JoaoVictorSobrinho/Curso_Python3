from time import sleep
num = int(input('Qual o valor que voce quer? '))
sleep(0.2)
print('Opções de transformação:'
      '\n1 - Binário'
      '\n2 - Octal'
      '\n3 - Hexadecimal')
t = int(input('\nDigite sua opção: '))

if t == 1:
    print('\n\033[33mBinário: {}'.format(bin(num)[2:]))
elif t == 2:
    print('\n\033[33mOctal: {}'.format(oct(num)[2:]))
elif t == 3:
    print('\n\033[33mHexadecimal: {}'.format(hex(num)[2:]))
else:
    print('\033[31mINVALIDA!!!\033[31m')

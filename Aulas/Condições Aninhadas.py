# Condições Aninhadas são uma expansão do "if & else"
# Apresentando uma solução para situações com mais de 2 opções
# if (se), else (senão), elif (senão se)
print('\033[32m-=-\033[m' * 15)
ano = float(input('Qual o ano do seu carro? '))
print('\033[32m-=-\033[m' * 15)
if ano <= 3:
    print('\033[32mSeu carro é novo!')
elif 3 < ano <= 5:
    print('\033[34mSeu carro é usado!')
else:
    print('\033[31mSeu carro é velho!')

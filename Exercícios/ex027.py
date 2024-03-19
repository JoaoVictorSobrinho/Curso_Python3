nome = str(input('Qual o seu nome completo? ')).strip().title()
nome_list = nome.split()
print(nome_list[0])
# Len conta quantidade, para saber posição basta subtrair 1
print(nome_list[len(nome_list) - 1])
print(nome_list)
print(len(nome_list))
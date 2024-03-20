l1 = float(input('Primeiro lado? '))
l2 = float(input('Segundo Lado? '))
l3 = float(input('Terceiro Lado? '))

if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print('O Triângulo é Válido!!')
    if l1 == l2 == l3:
        print('Equilátero')
    elif l1 == l2 or l1 == l3 or l2 == l3:
        print('Isósceles')
    # Pode ser escrito como l1 != l2 != l3 != l1
    else:
        print('Escaleno')
else:
    print('Não é possível formar um Triângulo')
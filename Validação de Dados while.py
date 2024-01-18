#EXERCICIO 57
player = ''
while player != 'M' and player != 'F':
    player = str(input('Digite seu sexo [M/F]: ')).upper().strip()[0]

    if player != 'M' and player != 'F':
        print('VOCE DIGITOU ERRADO! TENTE NOVAMENTE!')

if player == 'M':
    player = 'MASCULINO'

elif player == 'F':
    player = 'FEMININO'

print(f'Seu sexo é {player}')
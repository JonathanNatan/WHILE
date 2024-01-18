import random #IMPORTOU RANDOMIZAÇAO
'''c = 0 #CONTADOR
contador_venceu = 0 #CONTADOR VITORIAS

while True: 
    try:

        n = int(input('Digite um numero: ')) #INPUT
        if n <= 0:
            raise ValueError('Por favor, digite um numero positivo. ')

        escolher = str(input('Par ou impar [P/I]: ')).upper().split()[0] #ESCOLHA DE IMPAR PAR
        maquina = random.randint(1, n) #MAQUINA RANDOMIZADORA 
        s = maquina + n #SOMA
        
        print(f'Voce jogou {n} e a maquina jogou {maquina}. Total de {s} ') 

        if escolher == 'P' and s % 2 == 0: #SE FALOU PAR E DEU PAR
            print('Voce VENCEU!')
            contador_venceu += 1

        if escolher == 'P' and s % 2 == 1: # SE FALOU PAR E DEU IMPAR
            print('Voce PERDEU')

        if escolher == 'I' and s % 2 == 1: # SE FALOU IMPAR E DEU IMPAR
            print('Voce VENCEU!')
            contador_venceu += 1

        if escolher == 'I' and s % 2 == 0: #SE FALOU IMPAR E DEU PAR
            print('Voce PERDEU')
        c += 1 #CONTADOR

        if c == 3: #SE CONTADOR == 3 PARA E MOSTRA AS VITORIAS
            print(f'GAME OVER VOCE GANHOU {contador_venceu} VEZ(ES)')
            break
    except ValueError as e:
        print(f'Erro: {e}. Por favor, insira um numero positivo valido. ')
'''
import random

contador_vitorias = 0
c = 0

while True:
    # Entrada do usuário: digitar um número
    n = int(input('Digite um numero: '))

    # Geração de um número aleatório pela máquina entre 0 e 10
    maquina = random.randint(0, 10)

    # Inicialização da escolha como espaço em branco para garantir a entrada do loop
    escolher = ' '

    # Cálculo da soma entre o número digitado e o número aleatório gerado pela máquina
    total = maquina + n

    # Incremento do contador
    c += 1

    # Loop para garantir que o usuário escolha 'P' ou 'I'
    while escolher not in 'PI':
        escolher = str(input('PAR OU IMPAR: ')).upper().strip()[0]

    # Verificação da escolha do usuário e resultado do jogo
    if escolher == 'P':
        if total % 2 == 0:
            print('Voce VENCEU!')  
            print(f'Voce jogou {n} e a maquina jogou {maquina}. A soma foi {total} e deu PAR')
            contador_vitorias += 1
        else:
            print('Voce PERDEU')
            print(f'Voce jogou {n} e a maquina jogou {maquina}. A soma foi {total} e nao deu PAR')
    elif escolher == 'I':
        if total % 2 == 1:
            print('Voce VENCEU!')
            print(f'Voce jogou {n} e a maquina jogou {maquina}. A soma foi {total} e deu IMPAR')
            contador_vitorias += 1
        else:
            print('Voce PERDEU')
            print(f'Voce jogou {n} e a maquina jogou {maquina}. A soma foi {total} e nao deu IMPAR')     

    # Verificação do fim do jogo após 3 rodadas
    if c == 3:
        print(f'GAME OVER! VOCE VENCEU {contador_vitorias} vezes!')
        break

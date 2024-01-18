#EXERCICIO 58
import random

player = 11
aleatorio = random.randint(0, 10)
print('PENSEI EM UM NUMERO DE 0 A 10, TENTE ACERTAR QUAL FOI')

while player != aleatorio:
    player = int(input('Digite um numero de (0 a 10): '))
    
    if player > aleatorio:
        print('Tente um numero menor')
    
    if player < aleatorio:
        print('Tente um numero maior')

print('VOCE ACERTOU, E SEU PREMIO É NADA ')
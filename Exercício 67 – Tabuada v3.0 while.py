c = 0 #contador
n = int(input('Digite um numero: ')) #input
while True: #loop inf
    if n <= -1: #ponto de parada
        break
        print('Programa encerrado')
    c = c + 1
    m = n * c #multiplicação
    print(f'{n} x {c} = {m}') #mostrar a multiplacao enquanto o loop nao acabar 
    if c == 10: #se c == 10 roda isso
        n = int(input('Digite um numero: '))
        c = 0 #c é resetado
        
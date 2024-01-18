# Solicita ao usuário o número de termos desejados na sequência de Fibonacci
termos = int(input('Digite os termos: '))

# Inicializa os primeiros dois termos da sequência de Fibonacci
n1 = 0
n2 = 1

# Inicializa o contador para controlar o número de termos gerados
c = 3

# Imprime os dois primeiros termos
print(n1, end=' -> ')
print(n2, end=' -> ')

# Inicia um loop para gerar os termos subsequentes até atingir o número desejado de termos
while c <= termos:
    # Calcula o próximo termo somando os dois termos anteriores
    n3 = n1 + n2

    # Atualiza os dois termos anteriores para os próximos na sequência
    n1 = n2
    n2 = n3

    # Imprime o próximo termo
    print(n3, end=' -> ')

    # Incrementa o contador
    c = c + 1

# Imprime 'FIM' quando a sequência é gerada até o número desejado de termos
print('FIM')

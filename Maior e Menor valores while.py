n1 = 0             # Inicializa a variável n1 com 0 (não é estritamente necessário)
opcao = ''         # Inicializa a variável opcao como uma string vazia
c = 0              # Inicializa o contador c com 0 (para contar a quantidade de números digitados)
soma = 0           # Inicializa a variável soma com 0 (para acumular a soma dos números)
maior = 0          # Inicializa a variável maior com 0 (para rastrear o maior número digitado)
menor = 0          # Inicializa a variável menor com 0 (para rastrear o menor número digitado)

while opcao != 'N':  # Inicia um loop que continuará até que o usuário insira 'N'
    n1 = int(input('Digite um numero: '))  # Solicita ao usuário a entrada de um número e armazena em n1
    c += 1           # Incrementa o contador c para registrar a quantidade de números digitados
    soma = soma + n1 # Adiciona o valor de n1 à variável soma
    opcao = str(input('Digite se quer continuar ou nao [S/N]: ')).upper().strip()[0]  # Obtém 'S' ou 'N' para determinar se deseja continuar

    if soma == 1:    # Verifica se é a primeira entrada
        maior = n1   # Inicializa a variável maior com n1
        menor = n1   # Inicializa a variável menor com n1
    else:
        if n1 > maior: # Compara n1 com o valor atual de maior
            maior = n1  # Atualiza maior se n1 for maior
        if n1 < menor: # Compara n1 com o valor atual de menor
            menor = n1  # Atualiza menor se n1 for menor

    while opcao != 'S' and opcao != 'N':  # Garante que o usuário insira corretamente 'S' ou 'N'
        print('TENTE NOVAMENTE')
        opcao = str(input('Digite se quer continuar ou nao [S/N]: ')).upper().strip()[0]

        if opcao == 'N':
            break

media = soma / c   # Calcula a média dos números digitados
print(f'Voce digitou {c} valores e a Media dos numeros digitados foi {media:.2f}\n Maior valor foi {maior} e o menor foi {menor}')
print('fim')        # Imprime "fim" ao final do programa

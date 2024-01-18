#EXERCICIO 59
# Inicializando a opção com um valor diferente de 5 para iniciar o loop
opçao = 6

# Loop principal que executa até que a opção 5 (SAIR DO PROGRAMA) seja selecionada
while opçao != 5:
    
    # Solicita ao usuário para inserir dois números
    numero1 = int(input('Digite o primeiro numero: '))
    numero2 = int(input('Digite o segundo numero: '))

    # Inicializando o contador 'maior' com o valor de 'numero1'
    maior = numero1

    # Apresenta ao usuário as opções disponíveis
    print('Digite a opçao que voce quer\n1 = SOMA\n2 = MULTIPLICAÇÃO\n3 = NUMERO MAIOR\n4 = NOVOS NUMEROS\n5 = SAIR DO PROGRAMA')
    opçao = int(input('Digite sua opçao: '))

    # Verifica a opção escolhida pelo usuário e realiza a operação correspondente
    if opçao == 1:
        soma = numero1 + numero2
        print(f'A soma dos numeros {numero1} + {numero2} = {soma}')
    
    elif opçao == 2:
        multiplicacao = numero1 * numero2
        print(f'A multiplicação de {numero1} x {numero2} = {multiplicacao}')

    elif opçao == 3:
        # Compara os números e determina qual é o maior
        if numero2 > maior:
            maior = numero2
            print(f'O numero maior é {maior}')
        else:
            print(f'O numero maior é {maior}')

    elif opçao == 4:
        # Retorna ao início do loop, solicitando novos números ao usuário
        continue

# Quando a opção 5 é selecionada, o loop termina e esta mensagem é exibida
print('Voce terminou o programa!')

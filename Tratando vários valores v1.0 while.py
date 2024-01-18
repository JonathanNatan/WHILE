# Inicializa o contador 'c' com zero
c = 0

# Inicializa a variável 'soma' com zero
soma = 0

# Inicializa a variável 'termos' com zero
termos = 0

# Inicia um loop que continuará até que o usuário digite '999'
while termos != 999:
    # Solicita ao usuário um número para ser digitado
    termos = int(input('Digitador: '))
    
    # Verifica se o número digitado é diferente de '999'
    if termos != 999:
        # Adiciona o número à soma total
        soma = soma + termos
        
        # Incrementa o contador
        c = c + 1
    
    # Imprime 'COMPUTADOR' a cada iteração
    print('COMPUTADOR')

# Imprime o número de termos digitados e a soma total após o usuário digitar '999'
print(f'Você digitou {c} números e a soma entre eles foi {soma}')

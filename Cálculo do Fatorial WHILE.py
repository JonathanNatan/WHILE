#EXERCICIO 60
#from math import factorial
#player = int(input('Digite o factorial: '))
#resultado = factorial(player)
#print(resultado)


# Solicita ao usuário um número para calcular o fatorial
n = int(input('Digite um numero para calcular em factorial: '))

# Cria uma cópia do número fornecido para usar no loop enquanto ainda mantém o original
c = n

# Inicializa o fatorial como 1.
# A multiplicação começa com 1 porque qualquer número multiplicado por 1 resulta no próprio número.
f = 1  # Fator de multiplicação (fatorial)

# Enquanto c for maior que 0, o loop continuará executando.
while c > 0:
    # Imprime o valor atual de c (número em que estamos calculando o fatorial)
    print(c, end='')

    # Se c for maior que 1, imprime ' x ' para indicar multiplicação.
    # Se c for 1, imprime ' = ' para indicar o final da expressão.
    if c > 1:
        print(' x ', end='')
    else:
        print(' = ', end='')

    # Calcula o fatorial multiplicando o valor atual de f pelo valor atual de c.
    f = f * c

    # Decrementa o valor de c para a próxima iteração do loop.
    c = c - 1 

# Imprime o resultado final do fatorial.
print(f)  # Aqui, f contém o valor do fatorial de n.

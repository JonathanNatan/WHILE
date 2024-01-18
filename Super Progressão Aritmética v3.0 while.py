#EXERCICIO 62
# Solicita ao usuário o primeiro termo e a razão da progressão aritmética (PA).
primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Razao da pa: '))

# Inicializa o termo atual, um contador e variáveis para controle.
termo = primeiro       # Termo atual da PA.
cont = 1               # Contador para controlar a quantidade de termos exibidos.
total = 0              # Total de termos a serem exibidos em cada iteração.
mais = 10              # Quantidade de termos adicionais solicitados pelo usuário.

# Loop principal: Continua até o usuário decidir não adicionar mais termos (mais = 0).
while mais != 0:
    total = total + mais  # Atualiza o total de termos a serem exibidos.
    
    # Loop secundário: Exibe 'total' termos da PA.
    while cont <= total:
        print(termo, end=', ')  # Imprime o termo atual da PA.
        termo = termo + razao   # Atualiza o termo para o próximo da PA.
        cont = cont + 1          # Incrementa o contador de termos exibidos.
    
    print('PAUSA')                  # Indica pausa após exibir os termos.
    mais = int(input('Quantos termos voce quer adicionar? '))  # Solicita mais termos ao usuário.

print('fim')  # Indica o término do programa.

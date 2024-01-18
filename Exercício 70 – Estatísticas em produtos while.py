total = 0 #soma dos preços

contador_maismil = 0 #contador de produtos de mais de 1 k

menor = 0 #calcular menor variavel inicial
cont = 0
while True: #loop inf
    nome_produto = str(input('Nome do produto: ')) #input nome do produto
    preço = float(input('Preço: R$ ')) #preço
    cont += 1
    total = total + preço #soma

    if preço > 1000: #contador produtos mais de 1k
        contador_maismil += 1

    if cont == 1 or preço < menor:#qual menor preço e colocar o nome do produto nessa variavel
        menor = preço
        nome_barato = nome_produto
    opcao = ' ' #opcao começa com ' ' vazio 

    while opcao not in 'SN': # enquanto opcao nao for S ou N
        opcao = str(input('Quer continuar? [S/N] ')).upper().strip()[0] #repetir para sempre se nao for S ou N
 
    if opcao == 'N': #se opcao for igual a NAO, parar
        break

print(f'O produto mais barato foi {nome_barato} que custa R${menor}')
print(f'O total da compra foi {total:.2f}')
print(f'Temos {contador_maismil} produtos custando mais de R$ 1000')
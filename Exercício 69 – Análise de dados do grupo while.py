contador_maioridade = 0
contador_homens = 0
contador_menos20 = 0
while True:
    idade = int(input('Digite sua idade: '))
    if idade > 18:
        contador_maioridade += 1
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F]: ')).upper().strip()[0]
    if sexo == 'M':
        contador_homens += 1
    if sexo == 'F' and idade < 20:
        contador_menos20 += 1
    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if opcao == 'N':
        break
    if opcao == 'S':
        continue
print(f'Total de pessaos com mais de 18 anos: {contador_maioridade}\nAo todo temos {contador_homens} homens cadastrados\nE temos {contador_menos20} mulheres com menos de 20 anos')

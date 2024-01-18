sacar = int(input('Digite o quanto voce quer sacar: ')) #input player
cont50 = 0 #
cont20 = 0  #
cont10 = 0  # contadores de cedulas
cont1 = 0 #
maquina = sacar #maquina recebe o valor do player

while maquina >= 50: #enquanto o valor da maquina for maior ou igual a 50, ele vai diminuir 50 e contar 1 para cedulas
    maquina -= 50
    cont50 += 1
    
while maquina >= 20:
    maquina -= 20
    cont20 += 1

while maquina >= 10:
    maquina -= 10
    cont10 += 1

while maquina >= 1:
    maquina -= 1
    cont1 += 1

print(f'Cédulas de R$ 50: {cont50}')
print(f'Cédulas de R$ 20: {cont20}')
print(f'Cédulas de R$ 10: {cont10}')
print(f'Cédulas de R$ 1: {cont1}')
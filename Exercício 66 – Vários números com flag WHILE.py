s = 0
n = 0
c = 0
while True:
    n = int(input('Digite um valor [999 para parar]: '))
    if n == 999:
        break
    s += n
    c = c + 1
print(f'Voce {c} numeros e a soma deles foi {s}')
while True:
    numero = int(input('Digite um numero para ver sua tabuada'))
    if numero < 0:
        break
    for c in range(1,11):
        print(f'{numero} vezes {c} = {numero*c}')
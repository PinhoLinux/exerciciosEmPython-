cont = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
        'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove',
        'vinte')
while True:    
    num = int(input('Digite um numero ente 0 e 20: '))
    if 0 <= num <= 20:
        break
    print('Ocorreu um erro, tente novamente: ', end='')
print(f'Voce digitou o numero {cont[num]}')

print('Ocorreu um erro, tente novamente: ', end='')
print(f'Voce digitou o numero {cont[num]}')



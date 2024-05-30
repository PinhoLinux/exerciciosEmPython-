from random import randint
v = 0
while True:
    jogador = int(input('Digite um valor: '))
    computador = randint(0, 11)
    total = jogador + computador
    tipo = ''
    while tipo not in 'PI':
        tipo = str(input('Par ou impar? [P/I]')).strip().upper()[0]
    print(f'voce jogou {jogador} e o computador {computador}. total e {total} ', end='')
    print('DEU PAR' if total % 2 == 0 else 'DEU IMPAR' )
    if tipo == 'P':
        if total % 2 == 0:
            print(' Voce VENCEU! :(')
            V += 1
        else:
            print('Voce PERDEU! ;) ')
            break 
    elif tipo == 'I':
            if total % 2 == 1:
                print('Voce VENCEU! :(')
                V += 1 
            else:
                print('voce PERDEU! ;) ')
                break
    print('Vamo jogar novamente...')
print(f'GAMER OVER! Voce venceu {v} vezes.')

        
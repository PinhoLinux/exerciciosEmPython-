import random
import time
jogador = int(input('''escolha sua opção 
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA
Digite sua opção:
'''))
print('jo')
time.sleep(1)
print('ken')
time.sleep(1)
print('po!!!')
print('Analisandoo...')
time.sleep(5)
computador = random.randint(0,2)
if computador == 0:
  if jogador == 0:
    print('''
    jogador: pedra
    computador: pedra
    EMPATE''')

  if jogador == 1:
    print('''
    jogador: papel
    computador: pedra
    JOGADOR VENCEU''')
    
  if jogador == 2:
    print('''
    jogador: tesoura
    computador: pedra
    COMPUTADOR VENCEU''')

elif computador == 1:
  if jogador == 0:
    print('''
    jogador: pedra
    computador: papel
    COMPUTADOR VENCEU''')

  if jogador == 1:
    print('''
    jogador: papel
    computador: papel
    EMPATE''')
    
  if jogador == 2:
    print('''
    jogador: tesoura
    computador: papel
    JOGADOR VENCEU''')

elif computador == 2:
  if jogador == 0:
    print('''
    jogador: pedra
    computador: tesoura
    JOGADOR VENCEU''')

  if jogador == 1:
    print('''
    jogador: papel
    computador: tesoura
    COMPUTADOR VENCEU''')
    
  if jogador == 2:
    print('''
    jogador: tesoura
    computador: tesoura
    EMPATE''')

else:
  print('opção inválida')


  

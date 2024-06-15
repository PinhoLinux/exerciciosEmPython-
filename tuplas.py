# lanche = 'Hamburguer', 'suco', 'pizza', 'pudin'
# print(lanche[1])

# lanche = 'Hamburguer', 'suco', 'pizza', 'pudim'
# print(lanche[-3])

# lanche = ('Hamburguer', 'suco', 'pizza', 'pudim')
# print(lanche[1:3])

# lanche = ('Hamburguer', 'suco', 'pizza','pudim')
# tuplas sao imutáveis
# lanche[1] = refrigerante 
# print(lanche[-3:])

#lanche = ('Hamburguer', 'suco', 'pizza', 'pudim', 'batataa frita')
# print(lanche)

#for cont in range(0, len(lanche)):
    #print(f'Eu vou comer {lanche[cont]}')

# para nao aparecer "feinho" você pode fazer:
lanche = ('Hamburguer', 'suco', 'pizza', 'pudim', 'batataa frita')
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posicao {pos}')
print('como pra caramba!')

lanche = ('Hamburguer', 'suco','pizza','pudim', 'batata frita')

print(sorted(lanche))
print(lanche)

# observação: eu não mudei a tupla, eu apenas coloquei em ordem














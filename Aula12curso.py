nome = str(input("Digite seu nome: "))
if nome == "Emerson":
  print("Que nome lindo você tem!")
elif nome == 'pedro' or 'Guilherme' or 'Emerson'or 'Paulo':
  print('seu nome é muito comum')
else:
  print('seu nome é bem normal')
print('Bom dia, {}!'.format(nome))

# criar funções no python é um precesso simples e consiste em criar um bloco de codigo reutulizável que execulta tarefas especifica.
# No python usamos a palavra "def" para definir uma function

# 1 - def: plavra chave para criar a função
# 2 - nome_da_funcao: È o nome da sua função (deve ser único e descritivo)
# 3 - parametros: são os valores que você pode passar para a função (opicional)
# 4 - return: usado para retornar o resultado da função (opicional)

''' def somar(a, b):
    resultado = a + b
    return resultado

agora você pode usar ou "chamar" essa função:
print(somar(3, 5)) '''

# 1. funções sem parâmetros
# se sua funçãp nao precisar de informações externas, basta definila se, parâmetros:

'''def saudacao():
    print('Ola! eu estou entendendo tudo sobre funções!')
saudacao()'''

# 2. funções com parametros:

# se precisar passar valores para a função

'''def multiplicar(x, y):
    return x * y

print(multiplicar(4, 7))'''

# 3. funções com valores padrão
def apresentar(nome="pinho"):
    print(f'Ola, {nome}')

apresentar()
apresentar("Emerson")


















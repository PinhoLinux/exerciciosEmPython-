import time
idade = int(input('Digite sua idade:'))
print('■'*25)
print('Analisando sua idade, aguarde um momento:>')
print('■'*25)
time.sleep(5)
if idade < 18:
    print('Você é menor de idade :/')
else:
    print('você precisa se alistar no exército Brasileiro Imediatamente')
    print('Você deveria ter se alistado há {} anos'.format(idade - 18))

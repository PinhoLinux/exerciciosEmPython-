anoatual = 2024
nascimento = int(input('Digite o ano que vc nasceu:'))
idade= anoatual - nascimento

if idade > 9 and idade <= 13:
  
  print(' você tem {} anos sua classificação é atleta MIRIM'.format(idade))
  
elif idade > 14 and idade <= 18:
  
  print('você tem {} anos sua classificação é atleta INFANTIL'.format(idade))
  
elif idade > 19 and idade <= 24:
  
  print('você tem {} anos sua classificação é atleta JUNIOR'.format(idade))
  
elif idade == 25: 
  
  print('você tem {} anos sua classificação é atleta SÊNIOR'.format(idade))
  
elif idade < 25:
  
  print( 'você tem {} anos sua classificação é atleta MASTER'.format(idade))
  
  

larguraParede = float(input('Qual a largura da parede? '))
alturaParede = float(input('Qual a altura de parede?'))
area = larguraParede * alturaParede
tinta = area / 2
print(f'A parede tem a dimensão {larguraParede}X{alturaParede} e sua aréa é de {area:.2f}m²')
print(f'Para pintar essa parede você precisara de {tinta:.2f}l de tinta')


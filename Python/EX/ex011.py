altura = float(input('Altura da parede: '))
largura = float(input('Largura da parede: '))

area = altura * largura
tinta = area / 2 

print('''Sua parede tem dimensão de {}x{}, tem area de {}m2.
Para pintala são necessarios {} litros de tinta!'''.format(altura, largura, area, tinta))
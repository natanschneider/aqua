compra = float(input('Digite o valor da compra: R$'))
desconto = int(input('Agora digite o desconto: %'))

total = compra - (compra * desconto /100)

input('A compra de R${:.2f}, com {}% de desconto, fica: R${:.2f}!' .format(compra, desconto, total))
num = int(input('Digite um numero: '))
dobro = num * 2
triplo = num * 3 
raiz = num ** (1/2)

print('''O dobro de {}, é: {}.
O triplo de {} é: {}.
A raiz quadrada de {} é: {:.2f}.'''.format(num, dobro, num, triplo, num, raiz))
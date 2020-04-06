n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro: '))

soma = n1 + n2
multi = n1 * n2
divi = n1 / n2
di = n1 // n2

print('''A soma é: {}.
A Multiplicação é: {}.
A divisão é: {}.
O resto é: {}. ''' .format(soma, multi, divi, di))

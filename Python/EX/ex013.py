salario = float(input('Qual o salario do funcionario? R$'))
aumento = int(input('Quanto sera o aumento? %'))
total = salario + (salario * aumento /100)

print('Um funcionario que ganhava R${}, com aumento de {}%, passara a ganhar: R${:.2f}!'.format(salario, aumento, total))

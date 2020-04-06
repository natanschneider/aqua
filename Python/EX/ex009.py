num = int(input('Digite um numero para ver sua tabuada: '))

um = num * 1
dois = num * 2
tres = num * 3
quatro = num * 4
cinco = num * 5
seis = num * 6 
sete = num * 7
oito = num * 8 
nove = num * 9 
dez = num * 10
c = 10 * '-'

print('''{}
{}x 1 = {}
{}x 2 = {} 
{}x 3 = {} 
{}x 4 = {}
{}x 5 = {}
{}x 6 = {}
{}x 7 = {}
{}x 8 = {}
{}x 9 = {}
{}x10 = {}
{}''' 
.format(c, num, um, num, dois, num, tres, num, quatro, num, cinco, num, seis, num, sete, num, oito, num, nove, num, dez, c)) 
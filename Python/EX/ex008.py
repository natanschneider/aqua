m =float(input('Diga uma medida em metro: '))

dam = m / 10
hm = m / 100
km = m / 1000
dm = m * 10
cm = m * 100
mm = m * 1000

print('''{}dam
{}hm
{}km
{}dm 
{}cm
{}mm'''.format(dam, hm, km, dm, cm, mm))
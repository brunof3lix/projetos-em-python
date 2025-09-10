s = float(input('Salário: '))
p = float(input('Aumento%: '))
aumento = s + p / 100
novo = s + aumento
print (f'Aumento: {aumento:.2f}')
print (f'Novo Salário: R$ {novo:.2f}')

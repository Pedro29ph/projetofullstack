#transformaão de escalas de temperatura
print('seja bem-vindo ao programa de tranformaão de escala de temperatura')
escala= str(input('digite C para celso, F para fahrenheit e K para Kelvin'))
x= float(input('digite o valor que vai ser convertido'))

if escala== 'C' or escala== 'c':
    x1=x+273
    x2=((x*1.8)+32)
    print(f'valor em kelvin: {x1}')
    print(f'valor em fahrenheit: {x2}')
elif escala== 'F' or escala== 'f':
    x1= (x-32)/1.8
    x2=(((x-32)*0.555555556)+273)
    print(f'valor em celso: {x1}')
    print(f'valor em kelvin: {x2}')
else:
    x1=x-273
    x2= (((x-273)*1.8)+32)
    print(f'valor em celso: {x1}')
    print(f'valor em fahrenheit: {x2}')
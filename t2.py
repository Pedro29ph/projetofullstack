#diga o maior numero ente 3
n1= float(input( 'digite o priemira numero e aperte enter: '))
n2= float(input( 'digite o segunda numero e aperte enter: '))
n3= float(input( 'digite o terceira numero e aperte enter: '))

if n1>n2 and n1>n3:
    print (f'primeiro numero é o maior({n1})')
elif n2>n1 and n2>n3:
    print (f'segundo numero é o maior({n2})')
else:
    print (f'terceiro numero é o maior({n3})')
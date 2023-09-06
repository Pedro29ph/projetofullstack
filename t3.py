#diga se o numero é possitivo ou negativo
n=float(input( 'digite o numero e aperte enter: '))

if n>0:
    print(f'numero possitivo:{n}')
elif n<0:
    print(f'numero negativo:{n}')
else:
    print(f'numero neutro:{n}')
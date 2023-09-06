#diga a media de 4 notas
n1= float(input( 'digite sua priemira nota e aperte enter: '))
n2= float(input( 'digite sua segunda nota e aperte enter: '))
n3= float(input( 'digite sua terceira nota e aperte enter: '))
n4= float(input( 'digite sua quarta nota e aperte enter: '))

resu= (n1+n2+n3+n4)/4

if resu>=6:
     print (f'aluno aprovado com média {resu}')
elif resu>=4:
     print(f'aluno na recuperação com média {resu}')
else:
     print(f'aluno reprovado com média {resu}')
     
#receba f para feminino, m para masculino e exiba o sexo da pessoa 
sexo= str(input('digite M para se você é homem, F para mulher, T para trans e N para não especificar.'))

if sexo == 'M':
    print ('Homem')
elif sexo == 'F':
    print ('Mulher')
if sexo == 'T':
    print ('Trans')
elif sexo == 'N':
    print ('Não especificar')
#receba f para feminino, m para masculino e exiba o sexo da pessoa 
sexo= str(input('digite M para se você é homem, F para mulher, T para trans e N para não especificar.'))

if sexo == 'M' or sexo== 'm':
    print ('Homem')
elif sexo == 'F' or sexo== 'f':
    print ('Mulher')
if sexo == 'T' or sexo== 't':
    print ('Trans')
elif sexo == 'N' or sexo== 'n':
    print ('Não especificar')
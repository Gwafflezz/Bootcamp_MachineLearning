nota = float(input('Informe a nota do aluno: '))
comportado = True if input('comportado (y/n): ') == 'y' else False
 
if nota >= 9 and comportado:

    print('Duas palavras: para bens')
    print(' Quadro de honra')
    
elif nota >=7:
    print('aprovado')
elif nota>= 3.5:
    print('recuperação + trabalho')
else:
    print('reprovado')
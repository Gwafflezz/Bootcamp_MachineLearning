total = 0
nota = 0
qtde = 0

while nota != -1:
    nota = float(input('informe a nota ou -1 para sair: '))
    if nota != -1:
        qtde += 1
        total += nota

print(f'a media da turma eh: {total / qtde}')


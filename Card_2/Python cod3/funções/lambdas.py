from functools import reduce

alunos = [
    {'nome': 'ana', 'nota': 7.2},
    {'nome': 'breno', 'nota': 8.1},
    {'nome': 'Claudia', 'nota': 8.7},
    {'nome': 'Pedro', 'nota': 6.4},
    {'nome': 'Rafael', 'nota': 6.7},
]


def aluno_aprovado(aluno): return aluno['nota'] >= 7


def obter_nota(aluno): return aluno['nota']
somar = lambda a,b: a+b


alunos_aprovados = list(filter(aluno_aprovado, alunos))
notas_alunos_aprovados = list(map(obter_nota, alunos_aprovados))
total = reduce(somar, notas_alunos_aprovados, 0)

print(total / len(alunos_aprovados))

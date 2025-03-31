def soma(a, b):
    return a + b


def sub(a, b):
    return a - b


somar = soma
print(somar(3, 4))


def operacao_aritimetica(fn, op1, op2):
    return fn(op1, op2)


resultado = operacao_aritimetica(soma, 13, 48)
print(resultado)

resultado = operacao_aritimetica(sub, 13, 48)
print(resultado)


def soma_parcial(a):
    #calculo pesado1 - 10s
    #calculo pesado2 - 10s
    #calculo pesado3 - 40s
    def concluir_soma(b):
        return a+b # 10s
    return concluir_soma


resultado_final = soma_parcial(10)(12)
print(resultado_final)

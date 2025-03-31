def saudacao(nome=' pessoa', idade=20):
    print(f'bom dia {nome}! Vc nem parece ter {idade} anos!')

# def saudacao():
#     print(' boa tarde')


def soma_e_multi(a, b, x):
    return a + b * x  # precedência


if __name__ == '__main__':
    saudacao('ana', idade=30)

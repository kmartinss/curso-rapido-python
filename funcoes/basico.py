#!python3

def saudacao(nome = "pessoa", idade = 20):
    print(f'Bom dia, {nome}! Vc nem parece ter {idade} anos!')


def soma_e_multi(a, b, x):
    return a + b * x
    
print(__name__)

if __name__ == '__main__':
    saudacao('Karine', idade = 20)
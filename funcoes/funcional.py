def soma(a, b):
    return a + b

# somar = soma
# print(somar(3, 4))

def sub(a, b):
    return a - b


def operacao_aritmetica(fn, op1, op2):
    return fn(op1, op2)

result = operacao_aritmetica(sub, 20, 7)

print(result)


def soma_parcial(a):
    def concluir_soma(b):
        return a + b
    return concluir_soma

fn = soma_parcial(10)
result_final = fn(12)

print(result_final)
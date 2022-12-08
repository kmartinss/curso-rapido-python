#!python3

nota = float(input('Informe a nota do aluno: '))
bonzinho = True if input('Bonzinho (y/n): ') == 'y' else False

if nota >= 9 and bonzinho:
    print('Duas palavras: para béns! :P')
elif nota >= 7:
    print('Aprovado')
else:
    print('Burro')

print(nota)
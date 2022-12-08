#!python3

a = 'valor' # true
a = 0 # false
a = 00000.1  # true
a = '' # false
a = '  ' # true
a = [] # false

if a:
    print('existe')
else:
    print('Não existe ou é zero ou vazio...')
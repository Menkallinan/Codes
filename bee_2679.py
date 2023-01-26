'''
Para se preparar para os outros problemas, vamos fazer um teste. Dado um número X, retorne o menor número par maior do que X.

Entrada
Uma linha contendo um número  0 < X < 107.

Saída
Uma linha contendo a resposta do problema.
'''

a = int(input())

if (a % 2) == 0:
   a =  a + 2
else:
    a = a + 1

print(a)

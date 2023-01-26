'''
Leia 3 valores de ponto flutuante e efetue o cálculo das raízes da equação de Bhaskara. Se não for possível calcular as raízes, mostre a mensagem correspondente “Impossivel calcular”, caso haja uma divisão por 0 ou raiz de numero negativo.

Entrada
Leia três valores de ponto flutuante (double) A, B e C.

Saída
Se não houver possibilidade de calcular as raízes, apresente a mensagem "Impossivel calcular". Caso contrário, imprima o resultado das raízes com 5 dígitos após o ponto, com uma mensagem correspondente conforme exemplo abaixo. Imprima sempre o final de linha após cada mensagem.
'''
def bkaskara (a, b, c, delta):
    vetor_respostas = []
    delta = delta**(1/2)
    resposta1 = (-b + delta)/(2*a)
    resposta2 = (-b - delta)/(2*a)
    vetor_respostas.append(resposta1)
    vetor_respostas.append(resposta2)
    return vetor_respostas


a, b, c = [float(x) for x in input().split()]

delta = b**2 - (4*a*c)
if delta < 0 or a == 0:
    print('Impossivel calcular')
else:
    valor_respostas = []
    valor_respostas = bkaskara(a,b,c,delta)
    print('R1 = {:.5f}'.format(valor_respostas[0]))
    print('R2 = {:.5f}'.format(valor_respostas[1]))

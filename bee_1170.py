'''
No planeta Alpha vive a criatura Blobs, que come precisamente 1/2 de seu suprimento de comida disponível todos os dias. Escreva um algoritmo que leia a capacidade inicial de suprimento de comida (em Kg), e calcule quantos dias passarão antes que Blobs coma todo esse suprimento até restar um quilo ou menos.

Entrada
A primeira linha de entrada contem um único inteiro N (1 ≤ N ≤ 1000), indicando o número de casos de teste. As N linhas seguintes contém um valor de ponto flutuante C (1 ≤ C ≤ 1000) correspondente à quantidade de comida disponível para Blobs.

Saída
Para cada caso de teste, imprima uma linha contendo o número de dias que Blobs irá demorar para comer todo seu suprimento de comida, seguido da palavra "dias".
'''

def tempo(peso):
    dias = 0
    while peso/2 > 1:
        dias = dias + 1
        peso = peso/2

    dias = dias + 1
    return dias


quantidade = int(input())
contador = 0
valor= []


while contador < quantidade:
    peso = float(input())
    valor.append(tempo(peso))
    contador = contador + 1

contador =0

while contador < quantidade:
    print(valor[contador], "dias")
    contador = contador + 1

'''
Faça um programa que leia um vetor N[20]. Troque a seguir, o primeiro elemento com o último, o segundo elemento com o penúltimo, etc., até trocar o 10º com o 11º. Mostre o vetor modificado.

Entrada
A entrada contém 20 valores inteiros, positivos ou negativos.

Saída
Para cada posição do vetor N, escreva "N[i] = Y", onde i é a posição do vetor e Y é o valor armazenado naquela posição.
'''

vetor = []
for _ in range(20):
    valor=int(input())
    vetor.append(valor)
i =0
j = 19
while i != 10:
    valor = vetor[i]
    vetor[i] = vetor[j]
    vetor[j] = valor
    i = i + 1
    j = j - 1

i = 0
while i < 20:
    print("N[{}] =".format(i), vetor[i])
    i = i + 1

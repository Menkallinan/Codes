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

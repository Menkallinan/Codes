'''
Guilherme tem dez anos e é um pequeno entusiasta da matemática, e descobriu recentemente a existência dos famosos números primos. Com seu grande interesse pela disciplina, sua professora Marlene já lhe adiantou alguns conteúdos e um deles é o fatorial. Guilherme adora fazer exercícios e deseja treinar mais para preparar‐se para a Olimpíada de Matemática. Marlene passou uma lista de números para Guilherme resolver em casa, na qual todos os números primos encontrados deverão ser encontrados também seu respectivo fatorial. Ajude Guilherme a conferir seus exercícios e estudar para a Olimpíada

Entrada
A primeira linha da entrada contém um inteiro N indicando a quantidade de números a serem lidos. A segunda linha tem N números inteiros entre 1 e 100.

Limites:

1 ≤ N ≤ 100000;

Saída
A saída contém a quantidade de linhas representadas dos números que são primos, dentre os N números lidos. Em cada linha deve apresentar o número lido, seguido de um ponto de exclamação, um espaço, seguido por um sinal de igual, mais um espaço e o fatorial correspondente deste número
'''
def fatorial(numero):
        if numero == 2:
            return "2"
        elif numero == 3:
            return "6"
        elif numero ==  5:
            return "120";
        elif numero == 7:
            return "5040"
        elif numero ==  11:
            return "39916800"
        elif numero == 13:
            return "6227020800"
        elif numero == 17:
            return "355687428096000"
        elif numero == 19:
            return "121645100408832000"
        elif numero ==  23:
            return "25852016738884976640000"
        elif numero == 29:
            return "8841761993739701954543616000000"
        elif numero ==  31:
            return "8222838654177922817725562880000000"
        elif numero == 37:
            return "13763753091226345046315979581580902400000000"
        elif numero ==  41:
            return "33452526613163807108170062053440751665152000000000"
        elif numero == 43:
            return "60415263063373835637355132068513997507264512000000000"
        elif numero == 47:
            return "258623241511168180642964355153611979969197632389120000000000";
        elif numero ==  53:
            return "4274883284060025564298013753389399649690343788366813724672000000000000"
        elif numero ==  59:
         return "138683118545689835737939019720389406345902876772687432540821294940160000000000000"
        elif numero == 61:
            return "507580213877224798800856812176625227226004528988036003099405939480985600000000000000"
        elif numero == 67:
            return "36471110918188685288249859096605464427167635314049524593701628500267962436943872000000000000000"
        elif numero == 71:
            return "850478588567862317521167644239926010288584608120796235886430763388588680378079017697280000000000000000"
        elif numero == 73:
            return "4470115461512684340891257138125051110076800700282905015819080092370422104067183317016903680000000000000000"
        elif numero == 79:
            return "894618213078297528685144171539831652069808216779571907213868063227837990693501860533361810841010176000000000000000000"
        elif numero == 83:
            return "39455239697206586511897471180120610571436503407643446275224357528369751562996629334879591940103770870906880000000000000000000"
        elif numero == 89:
            return "16507955160908461081216919262453619309839666236496541854913520707833171034378509739399912570787600662729080382999756800000000000000000000"
        elif numero == 97:
            return '96192759682482119853328425949563698712343813919172976158104477319333745612481875498805879175589072651261284189679678167647067832320000000000000000000000'
        else:
            return '0'

n = int(input())
p = n
lista = []
numeros = []
x = [int(x) for x in input().split()]
i = 0
while i<n:
    if len(x)>i:
        if fatorial(x[i]) != '0':
            lista.append(fatorial(x[i]))
            numeros.append(x[i])

    i = i +1
tamanho = len(lista)
i = 0
while i < tamanho:
    print("{}! =".format(numeros[i]), lista[i])
    i = i +1

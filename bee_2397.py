'''
Caio estava brincando de construir triângulos com palitos de diferentes tamanhos. Ele fazia isso juntando as pontas de três palitos sobre uma mesa. Ele notou que podia agrupar os triângulos formados em três grupos:

Triângulos acutângulos, que são aqueles em que todos os ângulos internos medem menos de 90°;
Triângulos retângulos, que são aqueles que possuem um ângulo interno que mede exatamente 90°;
Triângulos obtusângulos, que são aqueles que possuem um ângulo interno que mede mais de 90°.
Ele também percebeu que nem sempre é possível formar um triângulo com três palitos.



Sua tarefa é, dados os comprimentos A, B e C de três palitos, dizer se é possível formar um triângulo com esses palitos e, em caso afirmativo, dizer a qual grupo o triângulo formado pertence.

Entrada
A entrada consiste de uma única linha, contendo três inteiros A, B e C (1 ≤ A, B, C ≤ 104) separados por espaço.

Saída
Imprima uma linha contendo apenas uma letra minúscula:

'n' se não for possível formar um triângulo;
'a' se o triângulo formado for acutângulo;
'r' se o triângulo formado for retângulo;
'o' se o triângulo formado for obtusângulo.
'''
def eh_obtusangulo(a, b ,c):
    a_angulo =((a**2)+ (b**2)-(c**2))/(2*a*b)
    b_angulo =((c**2)+ (b**2)-(a**2))/(2*c*b)
    c_angulo = ((c**2)+ (a**2)-(b**2))/(2*c*a)
    if (a_angulo < 0) or (b_angulo< 0) or (c_angulo < 0):
        return 1
    else:
        return 0


def tipo(a, b ,c):
    if (a**2 == b**2+ c**2) or (b**2 == a**2 + c**2) or (c**2 == a**2+b**2):
        return 'r'
    elif (a+b<=c) or (a+c<=b) or (b+c<=a):
        return 'n'
    else:
        d = eh_obtusangulo(a,b,c)
        if d == 1:
            return 'o'
        else:
            return 'a'



a, b, c = [int(x) for x in input().split()]
print(tipo(a,b,c))

'''
Leia a hora inicial, minuto inicial, hora final e minuto final de um jogo. A seguir calcule a duração do jogo.

Obs: O jogo tem duração mínima de um (1) minuto e duração máxima de 24 horas.

Entrada
Quatro números inteiros representando a hora de início e fim do jogo.

Saída
Mostre a seguinte mensagem: “O JOGO DUROU XXX HORA(S) E YYY MINUTO(S)” .
'''

h_i, m_i, h_f, m_f = [int(x) for x in input().split()]
dif = ((h_f*60)+m_f) - ((h_i*60)+m_i)
if dif <= 0:
    dif += 24*60
print("O JOGO DUROU {:.0f}".format(dif//60), "HORA(S) E {:.0f}".format(dif%60),"MINUTO(S)")

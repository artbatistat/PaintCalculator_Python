'''
Criar um programa que calcula a quantidade de tinta necessária para pintar uma parede.
O usuário deverá fornecer as seguintes informações : Rendimento da tinta, altura da parede e largura da parede.
O programa deve mostrar na tela a mensagem 'Você necessita de x latas de tintas'.
'''

def calcularTinta(rendimento,altura,largura):
    area_parede = altura * largura
    latas_total = area_parede / rendimento
    print(f'Você precisará de {latas_total} de latas de tinta')

rendimento_tinta = int(input('Qual o rendimento da tinta em m²?'))
altura_parede = int(input('Qual a altura da parede?'))
largura_parede = int(input('Qual a altura da parede?'))

calcularTinta(rendimento_tinta,altura_parede,largura_parede)



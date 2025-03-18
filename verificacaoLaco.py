"""
Faça uma função em Python para calcular a
área de um triângulo, usando a expressão:
area = (base * altura)/2.0
Faça um programa principal para testar essa
função e não permita a entrada de dados
inválidos, ou seja, medidas menores ou iguais
a zero.
Use o comando while para fazer a verificação
Essa hora-trabalho deve ser enviada para o professor antes
do próximo laboratório (terça-feira)


"""


base = int(input('Qual a base?: '))
altura = int(input('Qual a altura?: '))

while (base < 0) or (altura < 0):
    base = int(input('Por favor, informe a base corretamente: '))
    altura = int(input('Por favor, informe a altura corretamente: '))



def areaTriangulo(base, altura):
    return (base * altura) / 2


print(areaTriangulo(base, altura))

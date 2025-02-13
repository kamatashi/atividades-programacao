import math


area = 0
perimetroTriangulo = 0

def triangulo(a,b,c):
    global area
    global perimetroTriangulo
    sPerimetro = (a+b+c)/2
    area = math.sqrt(sPerimetro * (sPerimetro - a) * (sPerimetro - b) * (sPerimetro - c))
    perimetroTriangulo = sPerimetro*2


a = int(input('Qual o valor de a?: '))
b = int(input('Qual o valor de b?: '))
c = int(input('Qual o valor de c?: '))

triangulo(a,b,c)

print('O perimetro é: ', perimetroTriangulo)
print('A área dp triangulo é: ', area)

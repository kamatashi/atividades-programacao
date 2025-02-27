'''
Faça um programa principal em Python que receba
uma temperatura em graus Celsius (introduzida pelo
usuário no teclado) e apresente-a em graus
Fahrenheit, de acordo com a fórmula F = 1.8*C +
32.0
'''
celsius = float(input('Qual a temperatura em Celsius que gostaria de converter para Fahrenheit? '))

fahrenheit = 1.8*celsius + 32.0

print(fahrenheit)
'''
# Atividade 3
Faça uma função em Python que calcula o
fatorial de um número inteiro positivo através
de recursividade.
Faça um programa principal para testar a
função

'''

def fatorial(number):
    if number == 0:
        return number
    elif number == 1:
        return number
    else:
        return fatorial(number -1) * number
    

def teste(func, number):
    print(func(number))

teste(fatorial, 5)


'''
# Atividade 4
Faça uma função em Python que calcula o
fatorial de um número inteiro positivo através
de comando de repetição.
Faça um programa principal para testar a
função

'''

def fatorial2(number):
    result = 1
    while number > 1:
        result = number * result
        number = number -1
    return result

print(fatorial2(5))


'''
# Atividade 5
Faça uma função em Python que calcula a
soma dos números ímpares entre 1 e um
limite superior definido pelo usuário.
Faça um programa principal para testar a
função
'''

stop = int(input("Qual o limite? "))

def limit(number):
    acc = 0
    while number > 1:
        if (number % 2) == 0:
            number = number - 1
        else:
            acc = acc + 1
            number = number - 1
    return acc


print(limit(stop))

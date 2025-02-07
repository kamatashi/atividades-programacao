def somatorio(n, func):
    if n == 0:
        return 0
    func(n)
    return n + somatorio(n - 1, func)



def desvio():
    return


def addic(a,b=1):
    return a*b


resultado = somatorio(5,addic)

print(resultado)

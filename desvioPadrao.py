def somatorio(n, func):
    if n == 0:
        return 0
    return n + somatorio(n - 1)

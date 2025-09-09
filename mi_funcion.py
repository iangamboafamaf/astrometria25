import numpy as np
# %%
def suma(a, b, d = 0):
    '''
esta funcion suma a con b y opcionalmente d
parametros: a: numero
            b: numero
            d: numero (opcional)
            Devulve: c
modo de uso: c = suma(1, 2, d=4)
    '''
    c = a + b + d 
    return c

# %%
def glc(n, x0, a=57, c=1, M=256):
    numeros = []
    for i in range(n):
        x = (a*x0 + c) % M
        numeros.append(x/M)
        x0 = x
    return numeros
    '''
    # n va tomando valores 0,1,2,...,n-1 (for i in range(n))
    x = (c + a * x0) % M
    # el numero mas grande es M-1.
    # c es el incremento
    # a es la pendiente, x0 es la semilla
    # M es el modulo
    # n es la cantidad de numeros a generar
    '''

# %%
#generador de congruencial lineal
def congruencial_lineal_enteros(n, x0, a=1664525, c=1013904223, M=2**32):
    """Generador congruencial lineal de n números, semilla x0, parámetros a,c,M"""
    x = x0
    numeros = []
    for _ in range(n):
        x = (a*x + c) % M
        numeros.append(x)
    return numeros

def congruencial_lineal(n, x0, a=1664525, c=1013904223, M=2**32):
    return np.array(congruencial_lineal_enteros(n, x0, a, c, M))/M

# %%
#generador de fibonacci retardado
def fibonacci_enteros(n, x0, j=24, k=55, M=2**32):
    numeros = congruencial_lineal_enteros(k, x0)
    """Generador de Fibonacci de n números, semilla x0, retardos j,k y módulo M"""
    for i in range (k, k+n):
        numeros.append((numeros[i-j] + numeros[i-k]) % M)
    return numeros[k:]

def fibonacci(n, x0, j=24, k=55, M=2**32):
    return np.array(fibonacci_enteros(n, x0, j, k, M))/M

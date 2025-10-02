#%%
# mi_funcion2.py

def glc(n, x0, a=57, c=1, M=256, normalizado=True):
    """
    Genera n números del LCG: x_{n+1} = (a*x_n + c) mod M
    Si normalizado=True devuelve valores en [0,1) (float).
    Si normalizado=False devuelve enteros 0..M-1.
    """
    xs = []
    x = x0
    for _ in range(n):
        x = (a * x + c) % M
        xs.append(x / M if normalizado else x)
    return xs

def periodo_glc(x0, a=57, c=1, M=256):
    """
    Calcula el período detectando la primera repetición (trabaja con enteros).
    Devuelve un entero (periodo) o None si no encuentra repetición rápidamente.
    """
    visto = {}
    x = x0
    i = 0
    while True:
        i += 1
        x = (a * x + c) % M
        if x in visto:
            return i - visto[x]
        visto[x] = i
        # seguridad: si i supera M*2 salimos (no debería pasar para M pequeño)
        if i > M * 2:
            return None

def momentos(u, ks=(1,3,7)):
    """
    Calcula momentos empíricos E[u^k] para la lista u (valores en [0,1)).
    Devuelve dict {k: valor}.
    """
    n = len(u)
    out = {}
    for k in ks:
        out[k] = sum(x**k for x in u) / n if n > 0 else float("nan")
    return out
# %%

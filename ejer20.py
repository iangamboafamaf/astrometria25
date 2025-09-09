#%%
# # ej20 - Pearson para retardos 
import numpy as np
from mi_funcion import congruencial_lineal, fibonacci

def pearson_correlation(x, y):
    """Coeficiente de Pearson entre arrays (misma longitud)."""
    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)
    if x.shape != y.shape:
        raise ValueError("x e y deben tener la misma longitud")
    mx = x.mean(); my = y.mean()
    num = np.sum((x - mx) * (y - my))
    den = np.sqrt(np.sum((x - mx)**2) * np.sum((y - my)**2))
    return 0.0 if den == 0 else num / den

# parámetros
N = 10000
lags = [1, 2, 3, 5, 7, 10]

# generar secuencias 
seq_lcg = congruencial_lineal(N + max(lags), 142)
seq_fib = fibonacci(N + max(lags), 142)

def pearson_for_lags(u, lags):
    results = {}
    for L in lags:
        x = np.asarray(u[:-L], dtype=float)
        y = np.asarray(u[L:], dtype=float)
        results[L] = pearson_correlation(x, y)
    return results

res_lcg = pearson_for_lags(seq_lcg, lags)
res_fib = pearson_for_lags(seq_fib, lags)

print("Coeficiente de Pearson (retardos):")
print("Lag\tLCG\t\tFibonacci")
for L in lags:
    print(f"{L:>3d}\t{res_lcg[L]: .6f}\t{res_fib[L]: .6f}")

# %%

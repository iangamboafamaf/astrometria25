
# %%
from mi_funcion import fibonacci
import numpy as np
import matplotlib.pyplot as plt

def generador_galaxias(n):
    galaxias = []
    X = fibonacci(n, 142)
    for x in X:
        if (0 <= x) and (x < 0.4):
            galaxias.append("elíptica")
        elif (0.4 <= x) and (x < 0.7):
            galaxias.append("espiral")
        elif (0.7 <= x) and (x < 0.9):
            galaxias.append("enana")
        elif (0.9 <= x) and (x <= 1.0):
            galaxias.append("irregular")
    return galaxias

# %%
g = generador_galaxias(10000)

# Evito imprimir la lista completa (muy larga). Muestro conteos por tipo:
labels, counts = np.unique(g, return_counts=True)
print("Tipos y conteos:", list(zip(labels, counts)))

# %%
# Dibujo de barras con los conteos (reemplaza plt.hist(g) que no funciona con strings)
plt.bar(labels, counts)
plt.xlabel("Tipo de galaxia")
plt.ylabel("Frecuencia")
plt.title("Distribución generada de galaxias (N=10000)")
plt.show()

# %%

#%%

import numpy as np
import matplotlib.pyplot as plt

def sim_poisson_process(lam=5.0, T=3.0, rng=None):
    """
    Simula un proceso de Poisson  hasta tiempo T.
    Devuelve la lista de tiempos absolutos de los eventos.
    """
    if rng is None:
        rng = np.random.default_rng()
    t = 0.0
    events = []
    while True:
        u = rng.random()                    # U ~(0,1)
        inter = -np.log(1.0 - u) / lam      # tiempo entre eventos (inversa exponencial)
        t += inter
        if t <= T:
            events.append(t)
        else:
            break
    return events

# Parámetros
lam = 5.0           # tasa (eventos / h)
T = 3.0             # tiempo total (h)
n_experiments = 10000
rng = np.random.default_rng(42)   # semilla para reproducibilidad

# Simular muchas realizaciones y contar eventos en [0,T]
counts = [len(sim_poisson_process(lam, T, rng)) for _ in range(n_experiments)]

# Estadística 
print("Media muestral de N:", np.mean(counts))
print("Valor teórico E[N] = λ·T =", lam * T)

# Histograma (barras centradas en enteros)
maxN = max(counts)
bins = np.arange(0, maxN + 2) - 0.5   # para que las barras queden centradas en enteros
plt.figure(figsize=(8,4))
plt.hist(counts, bins=bins, density=True, edgecolor='black', alpha=0.7)
plt.title(f'Distribución de N en [0,{T}] — λ={lam} (simulación)')
plt.xlabel('Número de eventos N')
plt.ylabel('Frecuencia relativa')
plt.xticks(np.arange(0, maxN+1, step=max(1,int((maxN+1)/15))))
plt.show()

# %%

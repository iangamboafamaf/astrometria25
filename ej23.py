#%%
# ej23.py -- Ejercicio 23: suma de dos dados
import numpy as np
import matplotlib.pyplot as plt
from mi_funcion import congruencial_lineal
# ---------- parámetros ----------
N = 10000            # número de muestras para las comparaciones
seed_theo = 142      # semilla para muestreo desde la distribución teórica
seed_sim = 999       # semilla para simular lanzamiento de dados

# (a) espacio muestral y variable aleatoria 
print("a) Espacio muestral: {(i,j) : i=1..6, j=1..6}")
print("   Variable aleatoria X = suma de los dos dados, toma valores 2,3,...,12\n")

#(b) distribución teórica de la suma
sums = np.arange(2, 13)   # 2..12
# conteos teóricos: 1,2,3,4,5,6,5,4,3,2,1 (para 36 combinaciones)
counts_theo = np.array([1,2,3,4,5,6,5,4,3,2,1], dtype=float)
probs_theo = counts_theo / counts_theo.sum()
print("b) Distribución teórica (suma, probabilidad):")
for s, p in zip(sums, probs_theo):
    print(f"   {s:2d} : {p:.4f}")
print()

#(c) generar N valores de la variable usando la distribución teórica (transformada inversa)
# Generamos uniformes y las mapeamos a la distribución teórica mediante cortes acumulados
u = congruencial_lineal(N, seed_theo)   
u = np.array(u[:N], dtype=float)
cum = np.cumsum(probs_theo)              # cortes acumulados (distribución acumulada)

sampled_from_theo = np.empty(N, dtype=int)
for i, ui in enumerate(u):
    # buscamos el primer índice tal que ui < cum[idx]
    idx = np.searchsorted(cum, ui, side='right')
    sampled_from_theo[i] = sums[idx]

# conteo y proporciones empíricas del muestreo desde la distribución teórica
vals, counts = np.unique(sampled_from_theo, return_counts=True)
props = counts / N
print("c) Muestreo desde la distribución teórica (empírica):")
for s, c, pr in zip(vals, counts, props):
    print(f"   {s:2d}: count={c:5d}  prop={pr:.4f}")
print()

# (d) simular N experimentos de lanzar dos dados y calcular la suma
# Generamos 2*N uniformes y los mapeamos a enteros 1..6 por floor(u*6)+1
u2 = congruencial_lineal(2 * N, seed_sim)
u2 = np.array(u2[:2*N], dtype=float)
d1 = (u2[0::2] * 6).astype(int) + 1
d2 = (u2[1::2] * 6).astype(int) + 1
suma_sim = d1 + d2

vals_sim, counts_sim = np.unique(suma_sim, return_counts=True)
props_sim = counts_sim / N
print("d) Simulación directa de dos dados (empírica):")
for s, c, pr in zip(vals_sim, counts_sim, props_sim):
    print(f"   {s:2d}: count={c:5d}  prop={pr:.4f}")
print()

# gráficos: comparar (c) y (d) con la teoría
width = 0.35
xpos = np.arange(len(sums))

plt.figure(figsize=(10,4))
# teórico (probabilidades)
plt.bar(xpos - width/2, probs_theo, width=width, label='Teórico (prob)', color='C0')
# muestreo desde la distribución teórica (proporciones)
props_from_theo = np.array([props[np.where(vals == s)[0][0]] if s in vals else 0 for s in sums])
plt.bar(xpos + width/2, props_from_theo, width=width, label='Muestreo desde teórico', color='C1', alpha=0.8)
plt.xticks(xpos, sums)
plt.xlabel('Suma')
plt.ylabel('Probabilidad / Proporción')
plt.title('Comparación: teórico vs muestreo desde la distribución teórica')
plt.legend()
plt.tight_layout()
plt.show()

plt.figure(figsize=(10,4))
# teórico vs simulación directa
plt.bar(xpos - width/2, probs_theo, width=width, label='Teórico (prob)', color='C0')
props_sim_full = np.array([props_sim[np.where(vals_sim == s)[0][0]] if s in vals_sim else 0 for s in sums])
plt.bar(xpos + width/2, props_sim_full, width=width, label='Simulación directa (dados)', color='C2', alpha=0.8)
plt.xticks(xpos, sums)
plt.xlabel('Suma')
plt.ylabel('Probabilidad / Proporción')
plt.title('Comparación: teórico vs simulación directa de dados')
plt.legend()
plt.tight_layout()
plt.show()


# %%

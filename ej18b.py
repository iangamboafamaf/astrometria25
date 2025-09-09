#%%

import math
import mi_funcion as mf
import numpy as np
import matplotlib.pyplot as plt

# --- 1) Gráfico de pares sucesivos del congruencial 
numeros = mf.congruencial_lineal(1000, 142) 
x = numeros[1:]
y = numeros[:-1]
plt.plot(x, y, 'o')
plt.xlabel('$x_i$')
plt.ylabel('$x_{i-1}$')
plt.title('Generador Congruencial Lineal')
plt.axis('on')
plt.grid()
plt.show()

# --- 2) Caminatas aleatorias (K caminatas de N pasos) ---
N_caminatas = 100
N_pasos = 1000

# N_caminatas filas, N_pasos columnas
x = np.zeros((N_caminatas, N_pasos))
y = np.zeros((N_caminatas, N_pasos))

# Necesitamos 2*N_pasos números por caminata (dx, dy por paso).
# Genero una secuencia grande y la uso por bloques (misma semilla base).
numeros = mf.congruencial_lineal(2 * N_caminatas * N_pasos, 142)  
sqrt2 = np.sqrt(2.0)

# Recorrer caminatas
for i in range(N_caminatas):
    # cada caminata usa su bloque de números en 'numeros'
    base = i * 2 * N_pasos
    for j in range(1, N_pasos):
        # tomo dos números por paso: uno para dx, otro para dy
        u_dx = numeros[base + 2*j]       # índice par
        u_dy = numeros[base + 2*j + 1]   # índice impar

        salto_x = u_dx * 2 * sqrt2 - sqrt2   # mapea [0,1) -> [-sqrt2, sqrt2]
        salto_y = u_dy * 2 * sqrt2 - sqrt2

        x[i, j] = x[i, j-1] + salto_x
        y[i, j] = y[i, j-1] + salto_y

# --- 3) Dibujo de las trayectorias ---
plt.figure()
for i in range(N_caminatas):
    plt.plot(x[i, :], y[i, :])
plt.xlabel('x')
plt.ylabel('y')
plt.title(f'{N_caminatas} Caminatas Aleatorias de {N_pasos} pasos')
plt.grid()
plt.axis('equal')
plt.show()

# --- 4) Distancias y su promedio (expectación) ---
distancias = np.sqrt(x**2 + y**2)          # forma (K, N_pasos)

# Grafico de distancias por caminata y la media
plt.figure()
for i in range(N_caminatas):
    plt.plot(distancias[i], alpha=0.6)
plt.plot(np.mean(distancias, axis=0), 'k', lw=2, label='media sobre K')
plt.xlabel('Paso')
plt.ylabel('Distancia al origen')
plt.legend()
plt.title('Distancias por paso (cada caminata) y su media')
plt.show()

# Distancias finales (en el paso N_pasos-1) y estadística final
dist_final = np.sqrt(x[:, -1]**2 + y[:, -1]**2)
print(f'Distancias finales por caminata (K={N_caminatas}):')
print(dist_final)
print(f'Distancia final promedio: {np.mean(dist_final):7.3f}  +/- {np.std(dist_final):7.3f}')


# %%
# Constante teórica esperada para Δx,Δy en [-√2,√2]: sqrt(pi/3) ≈ 1.02333
cte_teor = math.sqrt(math.pi / 3.0)
print(f"\nConstante teórica sqrt(pi/3) = {cte_teor:.6f}")

# Graficar ⟨R⟩(n) y ⟨R⟩(n)/sqrt(n)
R_mean = np.mean(distancias, axis=0)
R_over_sqrt = R_mean / np.sqrt(np.arange(1, N_pasos+1))

plt.figure(figsize=(6,4))
plt.plot(np.arange(1, N_pasos+1), R_mean, label=r'$\langle R\rangle(n)$')
plt.xlabel("Paso n"); plt.ylabel(r'$\langle R\rangle$')
plt.legend()
plt.tight_layout()
plt.show()

plt.figure(figsize=(6,4))
plt.plot(np.arange(1, N_pasos+1), R_over_sqrt, label=r'$\langle R\rangle/\sqrt{n}$')
plt.hlines(cte_teor, 1, N_pasos, colors='k', linestyles='--', label='sqrt(pi/3) (teoría)')
plt.xlabel("Paso n"); plt.ylabel(r'$\langle R\rangle/\sqrt{n}$')
plt.legend()
plt.tight_layout()
plt.show()



# %%

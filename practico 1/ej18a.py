#%%
# main_simple.py
from mi_funcion2 import glc, periodo_glc, momentos

# Parámetros del ejercicio
a, c, M, semilla = 57, 1, 256, 10

# 1) Periodo
periodo = periodo_glc(semilla, a=a, c=c, M=M)
print("Período detectado:", periodo)

# 2) Genero N valores normalizados y calculo momentos para N=10,100,1000
for N in (10, 100, 1000):
    u = glc(N, semilla, a=a, c=c, M=M, normalizado=True)
    m = momentos(u, ks=(1,3,7))
    print(f"\nN = {N}")
    for k in (1, 3, 7):
        teorico = 1.0 / (k + 1)
        emp = m[k]
        print(f" k={k}: empírico={emp:.6f}  teórico={teorico:.6f}  error={abs(emp-teorico):.6f}")
# %%
# --- visualizaciones  ---
import matplotlib.pyplot as plt

# Usamos N=1000 para gráficos
Nplot = 100
u_plot = glc(Nplot, semilla, a=a, c=c, M=M, normalizado=True)

# 1) Scatter de pares sucesivos (u_n, u_{n+1})
plt.figure(figsize=(5,5))
plt.scatter(u_plot[:-1], u_plot[1:], s=6)
plt.title("Pares sucesivos (u_n, u_{n+1})")
plt.xlabel("u_n")
plt.ylabel("u_{n+1}")
plt.xlim(0,1)
plt.ylim(0,1)
plt.grid(True)
plt.tight_layout()
plt.show()

# 2) Histograma de la muestra u_n
plt.figure(figsize=(6,3))
plt.hist(u_plot, bins=30, density=True)
plt.title("Histograma de u_n (N={})".format(Nplot))
plt.xlabel("u")
plt.ylabel("densidad")
plt.tight_layout()
plt.show()
# %%
# prueba M grande de wikipedia
# https://en.wikipedia.org/wiki/Linear_congruential_generator#Parameters_in_common_use
a, c, M, semilla = 1664525, 1013904223, 2**32, 10
Nplot = 1000
u_plot = glc(Nplot, semilla, a=a, c=c, M=M, normalizado=True)
#grafico de pares sucesivos
plt.scatter(u_plot[:-1], u_plot[1:], s=6)
plt.title("LCG M grande (pares sucesivos)")
plt.show()
# histograma de la distribución
plt.hist(u_plot, bins=20, edgecolor="black")
plt.title("Histograma LCG M grande")
plt.xlabel("Valor generado")
plt.ylabel("Frecuencia")
plt.show()



# %%

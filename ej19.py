#%%
#ejercicio 19 (lagged Fibonacci)
import numpy as np
import matplotlib.pyplot as plt
from mi_funcion import fibonacci

N = 10000
semilla = 142   # la que se quiera

X = fibonacci(N, semilla)   

#  media y varianza muestral y comparación con teoría 
media_emp = np.mean(X)             # media empírica
var_emp_pop = np.var(X, ddof=0)    # varianza poblacional (divido por N)
var_emp_muestral = np.var(X, ddof=1)  # varianza muestral (divido por N-1)

media_teor = 0.5
var_teor = 1.0 / 12.0  # varianza de uniforme 1/12 ≈ 0.0833333

print("N =", N, "semilla =", semilla)
print(f"Media empírica = {media_emp:.6f}   (teórica = {media_teor:.6f})")
print(f"Var emp (poblacional, ddof=0) = {var_emp_pop:.6f}   (teórica = {var_teor:.6f})")
print(f"Var emp (muestral,   ddof=1) = {var_emp_muestral:.6f}")

#  Histograma y pares sucesivos para ver uniformidad y correlaciones
plt.figure(figsize=(6,3))
plt.hist(X, bins=50, density=True)
plt.title("Histograma: Fibonacci con retardo (N=10000)")
plt.xlabel("x"); plt.ylabel("densidad")
plt.tight_layout()
plt.show()

# pares sucesivos (scatter) X[i] vs X[i+1] para detectar correlaciones
plt.figure(figsize=(4.5,4.5))
plt.plot(X[:-1], X[1:], 'o', markersize=2)
plt.xlabel("X[n]"); plt.ylabel("X[n+1]")
plt.title("Pares sucesivos (X[n], X[n+1])")
plt.xlim(0,1); plt.ylim(0,1)
plt.grid(True)
plt.tight_layout()
plt.show()

# ---------- (g) Comparar con numpy.random.random() -------------------------
Y = np.random.default_rng(semilla).random(N)   # generador moderno (PCG64)

print("\nComparación con numpy.random:")
print(f"Media numpy = {np.mean(Y):.6f}   Var numpy = {np.var(Y,ddof=0):.6f}")

# Histogramas lado a lado
plt.figure(figsize=(10,3))
plt.subplot(1,2,1)
plt.hist(X, bins=50, density=True)
plt.title("Fibonacci (N=10000)")
plt.subplot(1,2,2)
plt.hist(Y, bins=50, density=True)
plt.title("numpy.random (N=10000)")
plt.tight_layout()
plt.show()

# %%

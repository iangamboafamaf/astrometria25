

# %%
import numpy as np
import matplotlib.pyplot as plt

# constante de Euler-Mascheroni (para comparar la media)
gamma = 0.5772156649015329

def gumbel(mu, beta, n, seed=42):
    np.random.seed(seed)                     
    u = np.random.uniform(0, 1, n)
    u = np.clip(u, 1e-15, 1 - 1e-15)         # evita log(0)
    x = mu - beta * np.log(-np.log(u))       # transformada inversa
    return x

# parámetros
mu = 0.0
beta = 1.0
n = 1000

# generar y verificar
samples = gumbel(mu, beta, n)
print("media muestral =", samples.mean())
print("media teórica  =", mu + gamma * beta)

# gráfico: histograma y pdf teórica
plt.hist(samples, bins=30, density=True, alpha=0.6)
x_vals = np.linspace(samples.min() - 0.5, samples.max() + 0.5, 200)
pdf = (1.0 / beta) * np.exp(-(x_vals - mu) / beta) * np.exp(-np.exp(-(x_vals - mu) / beta))
plt.plot(x_vals, pdf, lw=2)
plt.title("Gumbel (Fisher–Tippett)")
plt.show()


# %%

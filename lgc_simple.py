#%%
#!/usr/bin/env python3
# lcg_simple.py  -- generación LCG, período, momentos y scatter simple

from math import acos, sin, cos, radians, degrees
import matplotlib.pyplot as plt

# ---- funciones básicas ----
def lcg(a, c, M, x0):
    x = x0
    while True:
        x = (a * x + c) % M
        yield x

def lcg_normalized(a, c, M, x0):
    for xi in lcg(a, c, M, x0):
        yield xi / M

def sequence_until_repeat(a, c, M, x0, max_steps=1000000):
    seen = {}
    seq = []
    x = x0
    for i in range(max_steps):
        x = (a * x + c) % M
        if x in seen:
            period = i + 1 - seen[x]
            first_index = seen[x]
            return seq, period, first_index
        seen[x] = i + 1
        seq.append(x)
    return seq, None, None

def sample_moments(values, ks=(1,3,7)):
    res = {}
    n = len(values)
    for k in ks:
        res[k] = sum((x**k for x in values)) / n if n>0 else float('nan')
    return res

# ---- parámetros (los pedidos) ----
a, c, M, x1 = 57, 1, 256, 10

def main():
    # 1) período
    seq_int, period, first_index = sequence_until_repeat(a, c, M, x1, max_steps=10000)
    print(f"Parámetros: a={a}, c={c}, M={M}, semilla={x1}")
    print(f"Período detectado: {period}")
    print()

    # 2) primeros 20 valores normalizados
    first20 = seq_int[:20]
    print("Primeros 20 (x_n int) y normalizados u_n = x_n/M:")
    for i, xi in enumerate(first20, start=1):
        print(f"{i:2d}: {xi:3d}  u={xi/M:.6f}")
    print()

    # 3) momentos empíricos para N = 10,100,1000 y k = 1,3,7
    Ns = [10, 100, 1000]
    ks = [1, 3, 7]
    for N in Ns:
        gen = lcg_normalized(a, c, M, x1)
        vals = [next(gen) for _ in range(N)]
        moments = sample_moments(vals, ks)
        print(f"N = {N}")
        for k in ks:
            theoretical = 1.0/(k+1)
            print(f"  k={k}: empírico={moments[k]:.8f}  teórico={theoretical:.8f}  error={abs(moments[k]-theoretical):.8f}")
        print()

    # 4) scatter de pares sucesivos y guardado a PNG (N=10,100,1000)
    for N in Ns:
        gen = lcg_normalized(a, c, M, x1)
        vals = [next(gen) for _ in range(N+1)]
        xs = vals[:-1]
        ys = vals[1:]
        plt.figure(figsize=(4,4))
        plt.scatter(xs, ys, s=20)
        plt.title(f"Scatter (u_n, u_n+1) N={N}")
        plt.xlabel("u_n")
        plt.ylabel("u_{n+1}")
        plt.xlim(0,1)
        plt.ylim(0,1)
        plt.grid(True)
        fname = f"scatter_lcg_N{N}.png"
        plt.savefig(fname, dpi=150, bbox_inches='tight')
        print(f"Guardado: {fname}")
        plt.close()

if __name__ == "__main__":
    main()

# %%

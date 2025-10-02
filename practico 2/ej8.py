

# %%
import numpy as np
import math

def buffon_pi(l=1.0, t=1.0, n=10000, seed=42):
    """
    Estima pi con el experimento de Buffon usando np.random.random() y math.
    Supone l <= t (caso clásico).
    Devuelve (pi_est, prob, cruces).
    """
    np.random.seed(seed)
    cruces = 0
    for _ in range(n):
        x = (t / 2) * np.random.random()        # distancia al rayo más cercano, en [0, t/2]
        theta = (math.pi / 2) * np.random.random()  # ángulo agudo en [0, pi/2]
        if x <= (l / 2) * math.sin(theta):
            cruces += 1

    prob = cruces / n
    if cruces == 0:               # evita división por cero si no hubo cruces
        return float('nan'), prob, cruces

    pi_est = (2.0 * l) / (t * prob)
    return pi_est, prob, cruces

# Ejemplo
pi_est, prob, cruces = buffon_pi(l=1.0, t=1.0, n=100000, seed=123)
print("pi_est =", pi_est)
print("prob  =", prob)
print("cruces=", cruces)


# %%

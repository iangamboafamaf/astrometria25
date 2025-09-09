#%%
import matplotlib.pyplot as plt
import numpy as np
from mi_funcion import fibonacci
def ej19f1():  
    x = fibonacci(1000,142)
    _x = x[1:]
    _y = x[:-1]
    plt.plot(_x,_y,"ro")
#%%
ej19f1()
#%%
x = np.random.random(10)
print(x)
# %%
from mi_funcion import fibonacci
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
g = generador_galaxias(10000)
print(g)

# %%
def ej22():
    g = generador_galaxias(10000)
    print (np.unique(g, return_counts=True))
plt.hist(g)
# %%
def ejemplo():
    nombre = input("Ingrese su nombre: ")
    edad = int(input("Ingrese su edad: "))
    ano_de_nacimiento = 2025 - edad 
    print (f'su nombre es {nombre} y su año de nacimiento es {ano_de_nacimiento:7.2f}')
ejemplo()
# %%
def monty_hall():
    import random
    puertas = [0,0,1] # 0 = cabra, 1 = auto
    random.shuffle(puertas)
    eleccion_inicial = int(input("Elija una puerta (0, 1, 2): "))
    puertas_restantes = [i for i in range(3) if i != eleccion_inicial and puertas[i] == 0]
    puerta_abierta = random.choice(puertas_restantes)
    print(f"Se abre la puerta {puerta_abierta} y hay una cabra.")
    eleccion_final = int(input("¿Desea cambiar su elección a la otra puerta? (0, 1, 2): "))
    if puertas[eleccion_final] == 1:
        print("¡Felicidades! Ganaste un auto.")
    else:
        print("Lo siento, ganaste una cabra.")
# %%
monty_hall()
# %%

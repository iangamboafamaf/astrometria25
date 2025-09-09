#%%
# monty_hall.py
import random

def trial(switch: bool) -> bool:
    """Realiza un único juego. Devuelve True si el jugador gana."""
    prize = random.randrange(3)       # puerta con el auto (0,1,2)
    choice = random.randrange(3)      # elección inicial del jugador
    # el presentador abre una puerta con cabra distinta de la elegida y sin auto
    possible_to_open = [d for d in range(3) if d != choice and d != prize]
    host_opens = random.choice(possible_to_open)
    if switch:
        # cambiamos a la puerta que queda cerrada
        new_choice = next(d for d in range(3) if d != choice and d != host_opens)
        return new_choice == prize
    else:
        # mantenemos la elección inicial
        return choice == prize

def simulate(n: int = 1000):
    """Simula n juegos con y sin cambiar y muestra probabilidades empíricas."""
    wins_switch = sum(trial(True) for _ in range(n))
    wins_stay = sum(trial(False) for _ in range(n))
    print(f"Simulaciones: {n}")
    print(f"Cambiando:   {wins_switch}/{n} = {wins_switch/n:.4f}")
    print(f"Manteniendo: {wins_stay}/{n} = {wins_stay/n:.4f}")

if __name__ == "__main__":
    simulate(100000)   # cambia el número para más/menos precisión

# %%

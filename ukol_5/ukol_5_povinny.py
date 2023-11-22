# Mějme zadaný následující seznam naměřených teplot. Seznam obsahuje teploty naměřené pro každý den v týdnu ve čtyřech časech -
# ráno, v poledne, večer a v noci.

# 1. Vytvoř seznam průměrných teplot pro každý den.
import statistics

teploty = [
    [2.1, 5.2, 6.1, -0.1],
    [2.2, 4.8, 5.6, -1.0],
    [3.3, 6.5, 5.9, 1.2],
    [2.9, 5.6, 6.0, 0.0],
    [2.0, 4.6, 5.5, -1.2],
    [1.0, 3.2, 2.1, -2.0],
    [0.4, 2.7, 1.3, -2.8]
]

seznam_prumernych_teplot = [statistics.mean(den) for den in teploty]

print(seznam_prumernych_teplot)

# 2. Vytvoř seznam ranních teplot.
seznam_rannich_teplot = [den[0] for den in teploty]

print(seznam_rannich_teplot)

# 3. Vytvoř seznam nočních teplot.
seznam_nocnich_teplot = [den[3] for den in teploty]

print(seznam_nocnich_teplot)

# 4. Vytvoř seznam dvouprvkových seznamů obsahujících pouze polední a noční teplotu.
seznam_polednich_a_nocnich_teplot = [[den[1],den[2]] for den in teploty]

print(seznam_polednich_a_nocnich_teplot)
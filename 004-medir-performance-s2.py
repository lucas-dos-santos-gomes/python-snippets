# Snippet 4 - Como testar performance (série 2) - 27/11/2023

import timeit
time_test = timeit.repeat("[(a, b) for a in (1, 3, 5) for b in (2, 4, 6)]")
print("\nLista de tempos de execução:", time_test)
print("Tempo mínimo entre as repetições:", min(time_test), "\n")
# Snippet 4 - Como testar performance (série 2) - 27/11/2023

import timeit
time_test = timeit.repeat("[(a, b) for a in (1, 3, 5) for b in (2, 4, 6)]")
print("\nLista de tempos de execução:", time_test)
print("Tempo mínimo entre as repetições:", min(time_test), "\n")

# A função timeit.repeat executa a instrução passada como argumento várias vezes e retorna uma lista com os tempos de execução de cada execução. O min é usado para obter o tempo mínimo entre as repetições, o que geralmente é uma medida mais confiável do tempo de execução.
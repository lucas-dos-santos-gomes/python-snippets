# Snippet 5 - Como testar performance (série 3) - 04/12/2023

import cProfile
cProfile.run("[(a, b) for a in (1000, 3000000, 5000, 70000) for b in (2000, 400000000, 6000)]")

# A saída do cProfile.run() mostrará informações detalhadas sobre a chamada de função, o tempo gasto em cada função, o número de chamadas de função, entre outros dados. Essas informações são úteis para identificar partes do código que podem ser otimizadas em termos de desempenho. O cProfile é uma ferramenta poderosa para análise de desempenho em Python.
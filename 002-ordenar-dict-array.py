# Snippet 2 - Como ordenar uma lista de dicionários - 13/11/2023

d = {
  "chave1": 3,
  "chave2": 1,
  "chave3": 2.7085,
  "chave4": 10,
  "chave5": -5
}

new_dict = {
  k: v for k, v in sorted(d.items(), key=lambda item: item[1])
}

print(f"\nDicionário inicial: {d}")
print(f"Dicionário ordenado: {new_dict}\n")

"""
1- sorted(d.items(), key=lambda item: item[1]): Isso pega o dicionário d, converte-o em uma lista de tuplas chave-valor (usando items()) e classifica essas tuplas com base nos valores (elemento [1] da tupla) em ordem crescente.

2- {k: v for k, v in ...}: Isso cria um novo dicionário (new_dict) usando uma compreensão de dicionário. Ele percorre as tuplas (chave, valor) resultantes da ordenação e cria um novo dicionário onde as chaves permanecem as mesmas (k) e os valores também permanecem os mesmos (v).
"""
""" Snippet 1 - Como aplanar listas - 07/11/2023
Aplanar ou "flatten" significa transformar uma lista que pode conter listas aninhadas (do inglês "nested", são listas dentro de outras listas) em uma única linha unidimensional, onde todos os elementos estão no mesmo nível.
Por exemplo:

lista_aninhada = [1, [2, 3], [4, [5, 6]]]
lista_aplanada = [1, 2, 3, 4, 5, 6]
"""

def flatten_list(nested_list):
  if not(bool(nested_list)):
    return nested_list
  
  if isinstance(nested_list[0], list):
    return flatten_list(*nested_list[:1]) + flatten_list(nested_list[1:])
  
  return nested_list[:1] + flatten_list(nested_list[1:])

array = [1, 2, [10, 5, ["oi"], None, [True, 3j]]]
print(f"\nLista aninhada: {array}")
print(f"Lista aplanada: {flatten_list(array)}\n")
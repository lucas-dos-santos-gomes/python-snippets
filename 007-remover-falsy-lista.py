""" Snippet 7 - Como remover valores "falsy" de uma lista - 18/12/2023
Em Python, valores "falsy" são valores que são avaliados como False em um contexto booleano. Eles são usados em declarações condicionais e fluxo de controle para determinar se uma condição não é atendida. Aqui estão os valores "falsy" comuns em Python:

  1. False: O valor booleano False em si é um valor "falsy".
  2. None: O valor especial None, que representa a ausência de um valor, é "falsy".
  3. Zeros Numéricos: Valores numéricos iguais a zero são considerados "falsy". Isso inclui inteiros 0, números de ponto flutuante 0.0 e números complexos 0j.
  4.Sequências e Coleções Vazias:
    - Uma string vazia '' (uma string vazia é considerada "falsy", mas uma string não vazia é "truthy").
    - Uma lista vazia [].
    - Uma tupla vazia ().
    - Um dicionário vazio {}.
    - Um conjunto vazio set().
"""

falsyList = ['L', 0, 'u', 0.0, 'c', '', 'a', False, 's', None, ' ', 0j, 'G', [], 'o', (), 'm', {}, 'e', set(), 's']

def remove_falsy(unfiltered_list):
  return list(filter(bool, unfiltered_list))

print(f"\nLista padrão: {falsyList}")
print(f"Lista sem valores 'falsy': {remove_falsy(falsyList)}")
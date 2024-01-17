# Snippet 9 - Como inverter um dicionário (série 1) - 01/01/2024

dicionario = {
  "nome": "Lucas",
  "idade": 19,
  "cidade": "São Paulo",
  "estado": "SP",
  "cargo": "Aprendiz Administrativo",
  "estudante": True
}

# Essa função só funciona em dicionários que possuem valores únicos
dicionario_invertido = dict(map(reversed, dicionario.items()))

print(f"\nDicionário padrão: {dicionario}")
print(f"Dicionário invertido: {dicionario_invertido}\n")

"""
=> map: A função map é usada para aplicar uma função a cada elemento de um iterável (como uma lista) e retorna um novo iterável (geralmente uma lista) com os resultados da apicação da função a cada elemento.

=> reversed: A função reversed é usada para inverter a ordem dos elementos em um iterável, como uma lista. Ela retorna um objeto reverso que pode ser convertido em uma lista ou usado em um loop para iterar sobre os elementos na ordem inversa.
"""
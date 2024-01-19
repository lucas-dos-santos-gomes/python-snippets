# Snippet 11 - Como inverter um dicionário (série 3) - 15/01/2024

dicionario = {
  "nome": "Lucas",
  "idade": 19,
  "cidade": "São Paulo",
  "estado": "SP",
  "cargo": "Aprendiz Administrativo",
  "estudante": True
}

dic_invertido = {}

# Serve para dicionários com valores não únicos
{dic_invertido[v].append(k) for k, v in dicionario.items()}

print(f"\nDicionário padrão: {dicionario}")
print(f"Dicionário invertido: {dic_invertido}\n")

"""
=> for k, v in dicionario.items(): Isso itera sobre cada par chave-valor no dicionário dicionario. k representa a chave e v representa o valor.

=> dic_invertido[v].append(k): Isso cria ou atualiza uma entrada no dicionário dic_invertido usando o valor v como chave. Se a chave v já existe no dicionário, ele adiciona a chave original k a uma lista associada a essa chave. Se a chave v não existe no dicionário, cria uma nova entrada com o valor v como chave e uma lista contendo k como valor associado.
"""
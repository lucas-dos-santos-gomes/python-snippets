# Snippet 10 - Como inverter um dicionário (série 2) - 08/01/2024

dicionario = {
  "nome": "Lucas",
  "idade": 19,
  "cidade": "São Paulo",
  "estado": "SP",
  "cargo": "Aprendiz Administrativo",
  "estudante": True
}

dicionario_invertido = {
  value: key for key,
  value in dicionario.items()
}

print(f"\nDicionário padrão: {dicionario}")
print(f"Dicionário invertido: {dicionario_invertido}\n")

"""
=> dicionario.items(): Isso obtém uma sequência de tuplas, onde cada tupla é composta por um par chave-valor do dicionario.
=> for key, value in dicionario.items(): Isso itera sobre cada tupla da sequência, atribuindo a variável key à chave e a variável value ao valor do dicionário dicionario.
=> {value: key for key, value in dicionario.items()}: Isso cria um novo dicionário (dicionario_invertido) usando uma compreensão de dicionário. Para cada par chave-valor no dicionário original, ele inverte a ordem e usa o valor como a nova chave e a chave como o novo valor no dicionário resultante.
"""
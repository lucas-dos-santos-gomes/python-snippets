# Snippet 12 - Como inverter um dicionário (série 4) - 22/01/2024

dicionario = {
  "nome": "Lucas",
  "idade": 19,
  "cidade": "São Paulo",
  "estado": "SP",
  "cargo": "Aprendiz Administrativo",
  "estudante": True
}

dic_invertido = dict()

for key, value in dicionario.items():
  dic_invertido.setdefault(value, list()).append(key)

print(f"\nDicionário padrão: {dicionario}")
print(f"Dicionário invertido: {dic_invertido}\n")
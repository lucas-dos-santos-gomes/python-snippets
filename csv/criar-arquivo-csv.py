import csv

# Dados a serem escritos no arquivo CSV
dados = [
  ['NOME', 'IDADE', 'CIDADE'],
  ['Lucas', '19', 'Sao Paulo'],
  ['Maria', '30', 'Rio de Janeiro'],
  ['Pedro', '25', 'Belo Horizonte']
]

# Cria um arquivo CSV e escreve os dados nele
with open('data.csv', 'w', newline='') as arquivo_csv:
  writer = csv.writer(arquivo_csv)
  writer.writerows(dados)
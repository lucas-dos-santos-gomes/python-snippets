# Snippet 6 - Como visualizar um dataset - 10/12/2023

import pandas_profiling as pd

df = pd.read_csv("csv/data.csv")
profile = df.profile_report(title="Pandas Profiling Report")
profile.to_file(output_file="csv/output.html")

# A análise exploratória de dados é como um "check-up" dos dados antes de uma análise mais profunda. Ela ajuda a entender o que os dados têm a dizer, identificar problemas como erros ou valores estranhos, econtrar padrões e relações interessantes, e, finalmente, facilita a comunicação de descobertas. É o primeiro passo importante para garantir que suas análises sejam sólidas e relevantes. Em resumo, é como dar uma olhada rápida antes de mergulhar no mundo dos dados.

# Instalar pandas profiling
# pip install pandas-profiling
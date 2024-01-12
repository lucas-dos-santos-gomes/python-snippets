""" Snippet 3 - Como testar performance (série 1) - 20/11/2023
Neste exemplo, a performance foi medida com base nos tempos iniciais e finais de execução do código.
É importante testar o desempenho de um programa para garantir que ele atenda os requisitos de tempo e recursos, evite atrasos ou travamentos, e proporcione uam boa experiência do usuário. Testar o desempenho também ajuda a identificar gargalos e otimizar o código para melhor eficiência e economia de recursos. Isso resulta em aplicativos mais rápidos, econômicos e confiáveis.
"""

import datetime
start_time = datetime.datetime.now()
[(a, b) for a in range(1, 10000000, 2) for b in (2, 4, 6)] # Exemplo de trecho de código
end_time = datetime.datetime.now()
print(f"\n{end_time - start_time}\n")
import pandas as pd

import pandas as pd

df = pd.read_csv("https://github.com/BrunoSales95/DataSets/raw/main/dataset_barcos_real.csv", sep=';')
print(df.head)
df['preco'] = df['preco'].str.replace('$ ', '')  # Remove o símbolo de moeda
df['preco'] = df['preco'].str.replace('R', '')  # Remove o símbolo de moeda
df['preco'] = df['preco'].str.replace('.', '')    # Remove o ponto de milhar

df['nome_vendedor'] = df['nome_vendedor'].str.upper()
df['categoria'] = df['categoria'].str.upper()
df['fabricante'] = df['fabricante'].str.upper()
df['estado'] = df['estado'].str.upper()
df['anunciante'] = df['anunciante'].str.upper()
df['produto'] = df['produto'].str.upper()
df['pais'] = df['pais'].str.upper()
df['estado'] = df['estado'].str.upper()
df['cidade'] = df['cidade'].str.upper()
df.to_csv('dataset_barcos_transformado.csv', index = True, sep = ";")
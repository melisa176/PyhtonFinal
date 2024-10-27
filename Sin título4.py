import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('living.csv')
df.columns = df.columns.str.strip()

# 2
# Los 10 países con el costo de vida más alto
top_10_alto = df.sort_values(by='Cost of living, 2017', ascending=False).head(10)
plt.figure(figsize=(10, 6))
plt.barh(top_10_alto['Countries'][::-1], top_10_alto['Cost of living, 2017'][::-1])
plt.xlabel('Costo de Vida')
plt.title('Los 10 países con costo de vida más alto')
plt.show()

# Los 10 países con el costo de vida más bajo
top_10_bajo = df.sort_values(by='Cost of living, 2017', ascending=True).head(10)
plt.figure(figsize=(10, 6))
plt.barh(top_10_bajo['Countries'], top_10_bajo['Cost of living, 2017'])
plt.xlabel('Costo de vida')
plt.title('Los 10 países con costo de vida más bajo')
plt.show()

# Costo de vida de los países de América
paises_america = df[df['Continent'].str.contains('America', case=False, na=False)]
plt.figure(figsize=(12, 8))
plt.barh(paises_america['Countries'], paises_america['Cost of living, 2017'])
plt.xlabel('Costo de Vida')
plt.title('Costo de vida de los países de América')
plt.show()
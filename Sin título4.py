import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('living.csv')
df.columns = df.columns.str.strip()

# 1
# Número de filas y columnas y promedio
num_filas = df.shape[0]
num_columnas = df.shape[1]
costo_vida_promedio = df['Cost of living, 2017'].mean()

# País con el costo de vida más alto
pais_mas_alto = df.loc[df['Cost of living, 2017'].idxmax()]

# País con el costo de vida más bajo (corregido)
pais_mas_bajo = df.loc[df['Cost of living, 2017'].idxmin()]

# Costo de vida en Perú
costo_peru = df[df['Countries'].str.contains("Peru", case=False)]
ranking_peru = df.sort_values(by='Cost of living, 2017', ascending=False).reset_index(drop=True)
ranking_peru_idx = ranking_peru[ranking_peru['Countries'].str.contains("Peru", case=False)].index

print(f"Número de filas: {num_filas}")
print(f"Número de columnas: {num_columnas}")
print(f"Costo de vida promedio: {costo_vida_promedio:.2f}")
print(f"País con el costo de vida más alto: {pais_mas_alto['Countries']} ({pais_mas_alto['Cost of living, 2017']})")
print(f"País con el costo de vida más bajo: {pais_mas_bajo['Countries']} ({pais_mas_bajo['Cost of living, 2017']})")

if not costo_peru.empty:
    print(f"Costo de vida en Perú: {costo_peru.iloc[0]['Cost of living, 2017']}")
    if len(ranking_peru_idx) > 0:
        print(f"Ranking de Perú: {ranking_peru_idx[0] + 1}")

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
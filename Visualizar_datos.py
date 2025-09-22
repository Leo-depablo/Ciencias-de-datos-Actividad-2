import matplotlib.pyplot as plt
import seaborn as sns

# Configuración del estilo de los gráficos
sns.set_style("whitegrid")

# ==============================================================================
# 1. ¿Qué géneros y plataformas son los más populares?
# ==============================================================================
# Gráfico de ventas totales por género
plt.figure(figsize=(14, 6))
genre_sales = df.groupby('Genre')['Global_Sales'].sum().sort_values(ascending=False)
# Código corregido: asignamos y a hue y legend=False
sns.barplot(x=genre_sales.values, y=genre_sales.index, palette='viridis', hue=genre_sales.index, legend=False)
plt.title('Ventas Globales Totales por Género', fontsize=16)
plt.xlabel('Ventas Globales (en millones)', fontsize=12)
plt.ylabel('Género', fontsize=12)
plt.show()

# Gráfico de ventas totales por plataforma
plt.figure(figsize=(14, 8))
platform_sales = df.groupby('Platform')['Global_Sales'].sum().sort_values(ascending=False).head(10)
# Código corregido: asignamos y a hue y legend=False
sns.barplot(x=platform_sales.values, y=platform_sales.index, palette='mako', hue=platform_sales.index, legend=False)
plt.title('Top 10 de Plataformas por Ventas Globales', fontsize=16)
plt.xlabel('Ventas Globales (en millones)', fontsize=12)
plt.ylabel('Plataforma', fontsize=12)
plt.show()

# ==============================================================================
# 2. ¿Qué región domina el mercado?
# ==============================================================================
# Gráfico circular (pie chart) para comparar ventas por región
regional_sales = df[['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales']].sum()
plt.figure(figsize=(8, 8))
plt.pie(regional_sales, labels=regional_sales.index, autopct='%1.1f%%', startangle=140, colors=sns.color_palette('pastel'))
plt.title('Distribución de Ventas por Región', fontsize=16)
plt.show()

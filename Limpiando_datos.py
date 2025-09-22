import pandas as pd

# Cargar el archivo CSV
df = pd.read_csv(r"C:\Users\Leo\Desktop\vscode\ciencias de datos\actividad 2\dato.csv")

# ==============================================================================
# Paso 1: Limpiar las columnas de ventas
# ==============================================================================

# Reemplazar las comas (',') por puntos ('.') y convertir a tipo numérico (float)
# El método .astype(float) se usa para cambiar el tipo de dato.
for col in ['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales', 'Global_Sales']:
    df[col] = df[col].str.replace(',', '.').astype(float)

# ==============================================================================
# Paso 2: Manejar valores faltantes
# ==============================================================================

# Contar cuántos valores nulos hay en cada columna
print("\nValores nulos por columna (antes de la limpieza):")
print(df.isnull().sum())

# En este caso, la mejor opción es eliminar las filas con valores nulos, ya que
# son una minoría en un conjunto de datos grande.
df.dropna(inplace=True)

# ==============================================================================
# Paso 3: Verificar los cambios
# ==============================================================================

# Revisa la información del DataFrame de nuevo para confirmar que los tipos de datos han cambiado
print("\nInformación del DataFrame (después de la limpieza):")
df.info()

# Revisa las estadísticas descriptivas para ver si las columnas de ventas ahora aparecen
print("\nEstadísticas descriptivas (después de la limpieza):")
print(df.describe())

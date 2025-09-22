import pandas as pd

# Cargar el archivo CSV usando la ruta que proporcionaste.
try:
    df = pd.read_csv(r"C:\Users\Leo\Desktop\vscode\ciencias de datos\actividad 2\dato.csv")
    print("Archivo cargado exitosamente.")
except FileNotFoundError:
    print("Error: El archivo no se encontró en la ruta especificada.")
    # Usamos la "raw string" para que esta línea no dé error
    print(r"Asegúrate de que la ruta 'C:\Users\Leo\Desktop\vscode\ciencias de datos\actividad 2\dato.csv' sea la correcta.")
    exit()

# Muestra las primeras 5 filas para una primera vista.
print("\nPrimeras 5 filas del conjunto de datos:")
print(df.head())

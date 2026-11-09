# Iris Chavez NC = 0032   Fecha 6/11/2026
import pandas as pd
import numpy as np
print("Predicción de Precios de Inmuebles (Regresión) Iris Chavez NC = 0032")

# Datos del ejemplo
inmuebles = {
    "Id_Casa": [101, 102, 103, 104, 105, 106],
    "Metros_Cuadrados": [65, 120, 85, 200, 150, 95],
    "Habitaciones": [2, 4, 3, 5, 4, 3],
    "Precio_Miles_USD": [150, 310, 210, 480, 390, 240]
}

# Paso 1 y 2: Crear DataFrame
df = pd.DataFrame(inmuebles)
print(df)

# Paso 3: GroupBy Básico
print("*.*.*.*.*.*.*.*Agrupar por una sola columna NC 0032*.*.*.*.*.*.*.*")
grouped = df.groupby('Habitaciones')
print(grouped)

# Agregación
print(grouped['Precio_Miles_USD'].mean())
print(grouped['Metros_Cuadrados'].max())

# Paso 4: Agregaciones Múltiples
print("*.*.*.*.*.*.*.*Múltiples Agregaciones NC 0032*.*.*.*.*.*.*.*")
agg_result = grouped['Precio_Miles_USD'].agg(['mean', 'sum', 'max', 'min'])
print(agg_result)

# Paso 5: Agrupar por Múltiples Columnas
print("*.*.*.*.*.*.*.*Agrupar por múltiples columnas NC 0032*.*.*.*.*.*.*.*")
df['Zona'] = ['Norte', 'Sur', 'Norte', 'Sur', 'Norte', 'Sur']
grouped_multi = df.groupby(['Habitaciones', 'Zona'])['Precio_Miles_USD'].mean()
print(grouped_multi)

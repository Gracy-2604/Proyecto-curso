# Es apropiado usar el test de Kolmogorov-Smirnov en lugar del test de Shapiro-Wilk cuando la muestra de datos es muy grande, 
# cuando se desea comparar una muestra con una distribución teórica distinta de la normal o si se quiere comparar dos muestras empíricas
# pues permite comparar directamente las distribuciones sin asumir normalidad. Por su parte el test de Shapiro-Wilk si la muestra es pequeña 
# es más recomendable utilizarlo, pues es más preciso para detectar desviaciones de normalidad.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import shapiro, norm, probplot
import os

# Cargar datos

archivo = "Terminos_lagoon_TA_DIC_2023_RawData.csv"   
df = pd.read_csv("C:\\Users\\3g180\\Documents\\curso\\Semana_2\\Terminos_lagoon_TA_DIC_2023_RawData.csv")

# Crear carpeta para guardar resultados
os.makedirs("C:\\Users\\3g180\\Documents\\curso\\Semana_2\\graficos_normalidad", exist_ok=True)

# Variables
columnas_numericas = ["dic_micromol_kg", "sal_psu"]

# Guardar resultados estadísticos
resultados = []

# Evaluación Shapiro-Wilk)

for col in columnas_numericas:
    datos = df[col].dropna().values  
    
    if len(datos) < 3:
        continue  
    
    # Estadísticos descriptivos
    media = np.mean(datos)
    desviacion = np.std(datos, ddof=1)  
    
    # Shapiro-Wilk 
    stat_shapiro, p_shapiro = shapiro(datos)
    
    # Guardar en tabla
    resultados.append({
        "Variable": col,
        "N": len(datos),
        "Media": media,
        "Desviación estándar": desviacion,
        "Shapiro-Wilk stat": stat_shapiro,
        "Shapiro-Wilk p": p_shapiro,
        "Normalidad": "Normal" if p_shapiro > 0.05 else "No normal"
    })
    
    # Gráficas    
    # Histograma + curva normal
    plt.figure(figsize=(8,5))
    sns.histplot(datos, kde=True, stat="density", color="skyblue")
    x = np.linspace(min(datos), max(datos), 100)
    plt.plot(x, norm.pdf(x, media, desviacion), 'r', lw=2, label="Normal teórica")
    plt.title(f"Histograma - {col}")
    plt.legend()
    plt.savefig(f"graficos_normalidad/hist_{col}.png", dpi=300)
    plt.close()
    
    # Q-Q plot
    plt.figure(figsize=(6,6))
    probplot(datos, dist="norm", plot=plt)
    plt.title(f"Q-Q Plot - {col}")
    plt.savefig(f"graficos_normalidad/qq_{col}.png", dpi=300)
    plt.close()

# Guardar resultados
df_resultados = pd.DataFrame(resultados)
df_resultados.to_excel("C:\\Users\\3g180\\Documents\\curso\\Semana_2\\resultados_normalidad.xlsx", index=False)

print("Análisis completado con Shapiro-Wilk.")
print("Resultados guardados en 'resultados_normalidad.xlsx'")
print("Gráficos guardados en carpeta 'graficos_normalidad'")

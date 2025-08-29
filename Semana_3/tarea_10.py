import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import linregress
import os

# Cargar datos
archivo = "Terminos_lagoon_TA_DIC_2023_RawData.csv"
df = pd.read_csv("C:\\Users\\3g180\\Documents\\curso\\Semana_2\\Terminos_lagoon_TA_DIC_2023_RawData.csv")

# Crear carpeta para guardar gráficos
os.makedirs("C:\\Users\\3g180\\Documents\\curso\\Semana_3\\Graficas_Regresiones", exist_ok=True)

# Regresión lineal
def regresion_lineal(x, y, xlabel, ylabel, filename):
    # Eliminar NA
    data = df[[x, y]].dropna()
    
    # Calcular regresión
    slope, intercept, r_value, p_value, std_err = linregress(data[x], data[y])
    
    print(f"\n Regresión: {ylabel} vs {xlabel}")
    print(f" Ecuación: {ylabel} = {slope:.3f}*{xlabel} + {intercept:.3f}")
    print(f" R² = {r_value**2:.3f}, p-valor = {p_value:.3e}")
    
    # Gráfico
    plt.figure(figsize=(7,5))
    sns.regplot(x=x, y=y, data=data, scatter_kws={'alpha':0.6}, line_kws={"color":"red"})
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(f"Regresión lineal: {ylabel} vs {xlabel}\nR²={r_value**2:.3f}, p={p_value:.3e}")
    
    # Guardar
    plt.savefig(f"C:\\Users\\3g180\\Documents\\curso\\Semana_3\\Graficas_Regresiones/{filename}", dpi=300, bbox_inches="tight")
    plt.close()

# Aplicar regresion
# Salinidad vs Temperatura
regresion_lineal("sal_psu", "temp_c", "Salinidad (psu)", "Temperatura (°C)", "salinidad_vs_temp.png")

# DIC vs Salinidad
regresion_lineal("sal_psu", "dic_micromol_kg", "Salinidad (psu)", "DIC (µmol/kg)", "dic_vs_salinidad.png")

import pandas as pd
from scipy.stats import kruskal
import seaborn as sns
import matplotlib.pyplot as plt
import os

# Cargar datos
archivo = "Terminos_lagoon_TA_DIC_2023_RawData.csv"
df = pd.read_csv("C:\\Users\\3g180\\Documents\\curso\\Semana_2\\Terminos_lagoon_TA_DIC_2023_RawData.csv")

# Crear carpeta para guardar gráficos
os.makedirs("C:\\Users\\3g180\\Documents\\curso\\Semana_2\\Graficas_KruskalWallis", exist_ok=True)

# Aplicar Kruskal-Wallis
def kruskal_analysis(df, variable, group_col):
    resultados = []
    
    grupos = df[group_col].dropna().unique()
    if len(grupos) < 2:
        return pd.DataFrame()
    
    # Datos por grupo
    datos = [df[df[group_col] == g][variable].dropna() for g in grupos]
    
    if all(len(d) > 0 for d in datos):
        stat, p = kruskal(*datos)
        interpretacion = "Diferencia significativa (p<0.05)" if p < 0.05 else "No significativa (p≥0.05)"
        
        resultados.append({
            "Variable": variable,
            "Agrupador": group_col,
            "Estadístico H": stat,
            "p-valor": p,
            "Interpretación": interpretacion
        })
    return pd.DataFrame(resultados)

# Graficar
resultados_finales = []

for variable in ["dic_micromol_kg", "temp_c"]:
    for group_col in ["season", "area"]:
        
        res = kruskal_analysis(df, variable, group_col)
        if not res.empty:
            resultados_finales.append(res)
            
            # Boxplot
            plt.figure(figsize=(8,5))
            sns.boxplot(x=group_col, y=variable, data=df, palette="Set2")
            plt.title(f"Kruskal-Wallis of {variable} grouped by {group_col}")
            plt.savefig(f"C:\\Users\\3g180\\Documents\\curso\\Semana_2\\Graficas_KruskalWallis/{variable}_por_{group_col}.png", dpi=300, bbox_inches="tight")
            plt.close()

# Guardar resultados
 
if resultados_finales:
    resultados_df = pd.concat(resultados_finales, ignore_index=True)
    print(resultados_df)
    resultados_df.to_excel("C:\\Users\\3g180\\Documents\\curso\\Semana_2\\Resultados_KruskalWallis.xlsx", index=False)
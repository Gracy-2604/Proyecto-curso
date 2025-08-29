import pandas as pd
from scipy.stats import mannwhitneyu
import itertools
import seaborn as sns
import matplotlib.pyplot as plt
import os

# Cargar datos
archivo = "Terminos_lagoon_TA_DIC_2023_RawData.csv"  
df = pd.read_csv("C:\\Users\\3g180\\Documents\\curso\\Semana_2\\Terminos_lagoon_TA_DIC_2023_RawData.csv")

# Carpeta para guardar gráficas
os.makedirs("C:\\Users\\3g180\\Documents\\curso\\Semana_2\\Graficas_MannWhitney", exist_ok=True)

# Aplicar Mann-Whitney
def mann_whitney_analysis(df, variable, group_col, fixed_filter=None):
    resultados = []
    
    if fixed_filter:
        col, val = list(fixed_filter.items())[0]
        df = df[df[col] == val]
    
    grupos = df[group_col].unique()
    if len(grupos) < 2:
        return pd.DataFrame()
    
    for g1, g2 in itertools.combinations(grupos, 2):
        data1 = df[df[group_col] == g1][variable].dropna()
        data2 = df[df[group_col] == g2][variable].dropna()
        
        if len(data1) > 0 and len(data2) > 0:
            stat, p = mannwhitneyu(data1, data2, alternative="two-sided")
            interpretacion = "Diferencia significativa (p<0.05)" if p < 0.05 else "No significativa (p≥0.05)"
            
            resultados.append({
                "Variable": variable,
                "Grupo1": g1,
                "Grupo2": g2,
                "Estadístico U": stat,
                "p-valor": p,
                "Interpretación": interpretacion
            })
    return pd.DataFrame(resultados)

# Comparaciones
resultados_finales = []

# Comparar Estaciones dentro de cada Area
for area in df["area"].unique():
    for variable in ["dic_micromol_kg", "temp_c"]:
        res = mann_whitney_analysis(df, variable, "season", fixed_filter={"area": area})
        if not res.empty:
            res["Area"] = area
            resultados_finales.append(res)
            
            # Crear boxplot y violin plot
            sub_df = df[df["area"] == area]
            plt.figure(figsize=(8,5))
            sns.boxplot(x="season", y=variable, data=sub_df, palette="Set2")
            sns.violinplot(x="season", y=variable, data=sub_df, color="lightgray", inner=None, alpha=0.3)
            plt.title(f"{variable} - Comparison between seasons for the area {area}")
            plt.savefig(f"C:\\Users\\3g180\\Documents\\curso\\Semana_2\\Graficas_MannWhitney/{variable}_season_en_{area}.png", dpi=300, bbox_inches="tight")
            plt.close()

# Comparar Áreas dentro de cada Estación
for season in df["season"].unique():
    for variable in ["dic_micromol_kg", "temp_c"]:
        res = mann_whitney_analysis(df, variable, "area", fixed_filter={"season": season})
        if not res.empty:
            res["Season"] = season
            resultados_finales.append(res)
            
            # Crear boxplot y violin plot
            sub_df = df[df["season"] == season]
            plt.figure(figsize=(8,5))
            sns.boxplot(x="area", y=variable, data=sub_df, palette="Set3")
            sns.violinplot(x="area", y=variable, data=sub_df, color="lightgray", inner=None, alpha=0.3)
            plt.title(f"{variable} - Comparison between areas for the season {season}")
            plt.savefig(f"C:\\Users\\3g180\\Documents\\curso\\Semana_2\\Graficas_MannWhitney/{variable}_area_en_{season}.png", dpi=300, bbox_inches="tight")
            plt.close()

# Unir resultados y guardar
resultados_df = pd.concat(resultados_finales, ignore_index=True)
print(resultados_df)

# Guardar en Excel
resultados_df.to_excel("C:\\Users\\3g180\\Documents\\curso\\Semana_2\\Resultados_MannWhitney.xlsx", index=False)
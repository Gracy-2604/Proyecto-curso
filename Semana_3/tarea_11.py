from scipy.stats import pearsonr

def correlacion_pearson(x, y, nombre_x="Variable X", nombre_y="Variable Y"):
    """
    Calcula la correlación de Pearson entre dos variables.
    
    Parámetros:
    x, y : listas, arrays o Series de pandas
    nombre_x, nombre_y : nombres de las variables para mostrar
    
    Retorna:
    coeficiente, p-valor e interpretación
    """
    # Eliminar valores NA
    import pandas as pd
    df_temp = pd.DataFrame({nombre_x: x, nombre_y: y}).dropna()
    
    r, p = pearsonr(df_temp[nombre_x], df_temp[nombre_y])
    
    interpretacion = "Correlación significativa (p<0.05)" if p < 0.05 else "No significativa (p≥0.05)"
    
    resultado = {
        "Variable X": nombre_x,
        "Variable Y": nombre_y,
        "Coeficiente r": r,
        "p-valor": p,
        "Interpretación": interpretacion
    }
    
    return resultado

# Ejemplo
import pandas as pd

archivo = "Terminos_lagoon_TA_DIC_2023_RawData.csv"
df = pd.read_csv("C:\\Users\\3g180\\Documents\\curso\\Semana_2\\Terminos_lagoon_TA_DIC_2023_RawData.csv")

# Correlación Salinidad vs Temperatura
res1 = correlacion_pearson(df["sal_psu"], df["temp_c"], "Salinidad", "Temperatura")
print(res1)

# Correlación DIC vs Salinidad
res2 = correlacion_pearson(df["dic_micromol_kg"], df["sal_psu"], "DIC", "Salinidad")
print(res2)
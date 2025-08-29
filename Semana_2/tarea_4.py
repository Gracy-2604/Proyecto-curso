import pandas as pd

# Leer archivo CSV
df = pd.read_csv("C:\\Users\\3g180\\Documents\\curso\\Semana_2\\Terminos_lagoon_TA_DIC_2023_RawData.csv")

# Crear nueva columna 
df["TA_DIC_ratio"] = df["ta_micromol_kg"] / df["dic_micromol_kg"]

# Media y desviación por estación
resultados_estacion = df.groupby("season")["TA_DIC_ratio"].agg(
    media="mean",
    desviacion="std"
).reset_index()

# Media y desviación por estación y área 
resultados_estacion_area = df.groupby(["season", "area"])["TA_DIC_ratio"].agg(
    media="mean",
    desviacion="std"
).reset_index()

# Guardar en un archivo Excel
with pd.ExcelWriter("C:\\Users\\3g180\\Documents\\curso\\Semana_2\\TA_DIC_Season_Areas.xlsx") as writer:
    resultados_estacion.to_excel(writer, sheet_name="Season", index=False)
    resultados_estacion_area.to_excel(writer, sheet_name="Season_Area", index=False)

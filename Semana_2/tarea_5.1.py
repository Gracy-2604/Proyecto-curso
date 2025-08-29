# Histograma de dos variables juntas
import pandas as pd
import matplotlib.pyplot as plt

# Leer archivo
df = pd.read_csv("C:\\Users\\3g180\\Documents\\curso\\Semana_2\\Terminos_lagoon_TA_DIC_2023_RawData.csv")

# Datos a graficar
variable1 = df["dic_micromol_kg"]
variable2 = df["ta_micromol_kg"]

# Crear histograma superpuesto
plt.figure(figsize=(8,6))
plt.hist(variable1, bins=10, alpha=0.7, label="dic_micromol_kg", color="darkblue")
plt.hist(variable2, bins=10, alpha=0.5, label="ta_micromol_kg", color="skyblue")

# Títulos y etiquetas
plt.title("Histograma de dic_micromol_kg y ta_micromol_kg")
plt.xlabel("Valor")
plt.ylabel("Frecuencia")
plt.legend()

# Guardar imagen
plt.savefig("C:\\Users\\3g180\\Documents\\curso\\Semana_2\\histograma_dic_ta.png", dpi=300) 

# Mostrar histograma
plt.show()
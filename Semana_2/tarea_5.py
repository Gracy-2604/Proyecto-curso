import pandas as pd
import matplotlib.pyplot as plt

# Leer archivo CSV
df = pd.read_csv("C:\\Users\\3g180\\Documents\\curso\\Semana_2\\Terminos_lagoon_TA_DIC_2023_RawData.csv")

# Extraer columna que quieres graficar
datos = df["ta_micromol_kg"]

# Crear histograma
plt.hist(datos, bins=10, color='skyblue', edgecolor='black')

# Títulos y etiquetas
plt.title("Histograma de la variable 'ta_micromol_kg'")
plt.xlabel("ta_micromol_kg")
plt.ylabel("Frecuencia")

# Guardar imagen
plt.savefig("C:\\Users\\3g180\\Documents\\curso\\Semana_2\\histograma_ta.png", dpi=300) 

# Mostrar gráfico
plt.show()


# Leer archivo CSV
df = pd.read_csv("C:\\Users\\3g180\\Documents\\curso\\Semana_2\\Terminos_lagoon_TA_DIC_2023_RawData.csv")

# Extraer columna que quieres graficar
datos = df["dic_micromol_kg"]

# Crear histograma
plt.hist(datos, bins=10, color='darkblue', edgecolor='black')

# Títulos y etiquetas
plt.title("Histograma de la variable 'dic_micromol_kg'")
plt.xlabel("dic_micromol_kg")
plt.ylabel("Frecuencia")

# Guardar imagen
plt.savefig("C:\\Users\\3g180\\Documents\\curso\\Semana_2\\histograma_dic.png", dpi=300) 

# Mostrar gráfico
plt.show()
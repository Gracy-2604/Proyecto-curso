# Tarea_07
# ¿Cómo cambiar las unidades de las figuras?
# Tanto en Matplotlib o Seaborn las unidades de las figuras se controlan con el parámetro figsize que por defecto
# trabaja en pulgadas, pero si se desea también se pueden utilizar otra unidades de medida como cmm o mm.
# Ejemplo: 1 pulgada = 2.54 cm
# cm = 1/2.54  
# plt.figure(figsize=(15*cm, 10*cm))  # El tamaño sería 15x10 cm

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import os

# Leer archivo
archivo = "sisal_junio_2017.csv" 
df = pd.read_csv("C:\\Users\\3g180\\Documents\\curso\\Semana_2\\sisal_junio_2017.csv")

# Convertir a datetime
df["datetime"] = pd.to_datetime(df["fecha_hora"], format="%d/%m/%Y %H:%M")
df["dia"] = df["datetime"].dt.date

# Precipitación
df_precip = df.groupby("dia")["precipitation_mm"].sum().reset_index()
total_mes = df_precip["precipitation_mm"].sum()
media_diaria = df_precip["precipitation_mm"].mean()

# Temperatura 
df_temp = df.groupby("dia")["temperatura_c"].agg(["max", "min"]).reset_index()

# Crear carpeta para guardar las gráficas
carpeta = r"C:\\Users\\3g180\\Documents\\curso\\Semana_2\\Graficas_Sisal_junio_2017"
os.makedirs(carpeta, exist_ok=True) 

# Gráfico_Precipitación 
plt.figure(figsize=(12,6))
sns.barplot(data=df_precip, x="dia", y="precipitation_mm", color="royalblue")
plt.axhline(media_diaria, color="red", linestyle="--", label=f"Media diaria = {media_diaria:.2f} mm")
plt.title(f"Precipitación diaria\nTotal mensual = {total_mes:.2f} mm")
plt.xlabel("Día")
plt.ylabel("Precipitación (mm)")
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.savefig(os.path.join(carpeta, "precipitacion_diaria.png"), dpi=300)
plt.close()

# Gráfico_Temperatura 
plt.figure(figsize=(12,6))
plt.plot(df_temp["dia"], df_temp["max"], label="Temp. Máxima", color="darkorange", marker="o")
plt.plot(df_temp["dia"], df_temp["min"], label="Temp. Mínima", color="royalblue", marker="o")
plt.title("Temperatura diaria (Máx vs Mín)")
plt.xlabel("Día")
plt.ylabel("Temperatura (°C)")
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.savefig(os.path.join(carpeta, "temperatura_diaria.png"), dpi=300)
plt.close()

# Gráfico_Rosa de los vientos 
wind_dir_rad = np.deg2rad(df["wind_dir_deg"])
wind_speed = df["wind_speed_m_s"]

# Definir intervalos de velocidad (m/s)
bins = [0, 2, 4, 6, 8, 10, 20]
labels = ["0-2", "2-4", "4-6", "6-8", "8-10", "10+"]
df["vel_bin"] = pd.cut(wind_speed, bins=bins, labels=labels, right=False)

# Colores para cada categoría
colors = sns.color_palette("viridis", len(labels))

plt.figure(figsize=(8,8))
ax = plt.subplot(111, polar=True)
ax.set_theta_zero_location("N")
ax.set_theta_direction(-1)

# Graficar histograma circular por categorías
for (cat, color) in zip(labels, colors):
    subset = df[df["vel_bin"] == cat]
    ax.hist(np.deg2rad(subset["wind_dir_deg"]), bins=36,
            weights=np.ones(len(subset)),  # cuenta de ocurrencias
            color=color, alpha=0.8, label=cat)

plt.title("Rosa de los vientos")
plt.legend(title="Velocidad (m/s)", bbox_to_anchor=(1.1, 1.05))
plt.tight_layout()
plt.savefig(os.path.join(carpeta, "rosa_vientos.png"), dpi=300)
plt.close()

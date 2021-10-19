import folium
import pandas as pd
import os
variable="index.html"
variable2="Eventos.csv"
eventos = pd.read_csv(os.path.abspath(variable2))
def ocurrencia(row):
    if row["Cantidad de gente"] < 10:
        return "green"
    elif row["Cantidad de gente"] >= 10 and row["Cantidad de gente"] < 30:
        return "orange"
    else:
        return "red"
eventos["Ocurrencia"] = eventos.apply(ocurrencia, axis=1)    
mapita = folium.Map(location=[-36.8939975,-60.3227331], zoom_start=7)
for _, evento in eventos.iterrows():
    folium.Marker(location=[float(evento["Latitud"]), float(evento["Longitud"])],
    tooltip=(evento["Nombre"]), 
    icon=folium.Icon(color=evento["Ocurrencia"]), 
    popup=evento["Cantidad de gente"]).add_to(mapita)                                  
mapita.save(os.path.abspath(variable))
os.system("index.html")

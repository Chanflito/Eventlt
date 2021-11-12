import folium
import pandas as pd
import os
import sys , subprocess
variable="index.html"
variable2="Eventos.csv"
eventos = pd.read_csv(os.path.abspath(variable2))

class Mapa():
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
        texto= f'''gente en la zona: {evento["Cantidad de gente"]}<br>
        hola<br>
        3rd line'''      #todo lo que yo agregue adentro del f'', va a imprimirse en el popup del mapa
        folium.Marker(location=[float(evento["Latitud"]), float(evento["Longitud"])],
        tooltip=(evento["Nombre"]), 
        icon=folium.Icon(color=evento["Ocurrencia"]), 
        popup = folium.Popup(texto, min_width=300, max_width=300)).add_to(mapita) 
    mapita.save(os.path.abspath(variable))
    def show_map ():
        if os.sys.platform == "win32":
            return os.startfile("index.html") #Open map with Windows System.
        else:
            opener = "open" if os.sys.platform == "darwin" else "xdg-open" #Open map wtih OSX system.
            return subprocess.call([opener, "index.html"])

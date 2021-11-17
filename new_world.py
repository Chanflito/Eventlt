import folium
import pandas as pd
import os
import sys , subprocess


class Mapa():
    @staticmethod
    def show_map (lat, lon):
        marcadores = "marcadores.csv"
        i = 0
        df_marcador = pd.read_csv(os.path.abspath(marcadores))
        mapita = folium.Map(location=[lat,lon], zoom_start=15, dragging=False)
        for _, marcador in df_marcador.iterrows():
            folium.Marker(location=[float(marcador["Latitud"]), float(marcador["Longitud"])],
            tooltip=(marcador["Nombre"]), 
            icon=folium.Icon(color='blue'), 
            popup = folium.Popup(marcador["Descripcion"], min_width=300, max_width=300)).add_to(mapita) 
            i += 1
        mapita.save(os.path.abspath("index.html"))
        
        if os.sys.platform == "win32":
            return os.startfile("index.html") #Open map with Windows System.
        else:
            opener = "open" if os.sys.platform == "darwin" else "xdg-open" #Open map wtih OSX system.
            return subprocess.call([opener, "index.html"])

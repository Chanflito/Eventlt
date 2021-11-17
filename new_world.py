import folium
import pandas as pd
import os
import sys , subprocess
from folium.plugins import MarkerCluster
mc=MarkerCluster()
df_marcador = pd.read_csv(os.path.abspath("marcadores.csv"))

class Mapa():
    @staticmethod
    def show_map (lat, lon):
        i = 0
        mapita = folium.Map(location=[lat,lon], zoom_start=15, dragging=False)
        for _, marcador in df_marcador.iterrows():
            mapita.add_child(folium.Marker(location=[float(marcador["Latitud"]), float(marcador["Longitud"])],
            tooltip=(marcador["Nombre"]), 
            icon=folium.Icon(color='blue'), popup = folium.Popup(marcador["Descripcion"], min_width=300, max_width=300)))
            i += 1
        mapita2 = folium.Map(location=[-36.8939975,-60.3227331], zoom_start=7)
        for _, marcador in df_marcador.iterrows():
            mc.add_child(folium.Marker(location=[float(marcador["Latitud"]), float(marcador["Longitud"])],
            tooltip=(marcador["Nombre"]), popup=marcador["Descripcion"]))
        mapita2.add_child(mc)
        mapita2.save(os.path.abspath("index.html"))
        
        if os.sys.platform == "win32":
            return os.startfile("index.html") #Open map with Windows System.
        else:
            opener = "open" if os.sys.platform == "darwin" else "xdg-open" #Open map wtih OSX system.
            return subprocess.call([opener, "index.html"])

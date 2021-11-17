import folium
import pandas as pd
import os
import subprocess
from folium.plugins import MarkerCluster
from listaDeEventos import eventos
mc = MarkerCluster()
df_marcador = pd.read_csv(os.path.abspath("marcadores.csv"))


class Mapa():
    
    @staticmethod
    def popupHelper(i):
        newText = ''
        for a in eventos.list[i]:        #<strong> texto </strong>
            newText += f'''<strong> {a.description} </strong><br>'''
        return newText

    @staticmethod
    def show_map (lat, lon):
        
        mapita = folium.Map(location=[lat,lon], zoom_start=15)
        for _, marcador in df_marcador.iterrows():
            mc.add_child(folium.Marker(location=[float(marcador["Latitud"]), float(marcador["Longitud"])],
            tooltip=(marcador["Nombre"]), popup = folium.Popup( marcador["Descripcion"], min_width=300, max_width=300)))
            
        mapita.add_child(mc)
        mapita.save(os.path.abspath("index.html"))
        
        if os.sys.platform == "win32":
            return os.startfile("index.html") #Open map with Windows System.
        else:
            opener = "open" if os.sys.platform == "darwin" else "xdg-open" #Open map wtih OSX system.
            return subprocess.call([opener, "index.html"])

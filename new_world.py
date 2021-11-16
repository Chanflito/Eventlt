import folium
import pandas as pd
import os
import sys , subprocess
variable="index.html"
variable2="Eventos.csv"
marcadores = "marcadores.csv"
eventos = pd.read_csv(os.path.abspath(variable2))
from listaDeEventos import eventos as listaDeEventos

class Mapa():
    
    @staticmethod
    def popupHelper(i):
        newText = ''
        for a in listaDeEventos.list[i]:                              #<strong> texto </strong>
            newText += '<strong>' + a.description + '<\strong><br>'
        return newText
    
    @staticmethod
    def show_map (lat, lon):
        df_marcador = pd.read_csv(os.path.abspath(marcadores))
        mapita = folium.Map(location=[lat,lon], zoom_start=15, zoom_control=False, scrollWheelZoom=False, dragging=False)
        
        i = 0
        for _, marcador in df_marcador.iterrows():
            texto= Mapa.popupHelper(i)    #todo lo que yo agregue adentro del f'''   ''', va a imprimirse en el popup del mapa
            folium.Marker(location=[float(marcador["Latitud"]), float(marcador["Longitud"])],
            tooltip=(marcador["Nombre"]), 
            icon=folium.Icon(color='blue'), 
            popup = folium.Popup(texto, min_width=300, max_width=300)).add_to(mapita) 
            i += 1
        mapita.save(os.path.abspath(variable))
        
        if os.sys.platform == "win32":
            return os.startfile("index.html") #Open map with Windows System.
        else:
            opener = "open" if os.sys.platform == "darwin" else "xdg-open" #Open map wtih OSX system.
            return subprocess.call([opener, "index.html"])

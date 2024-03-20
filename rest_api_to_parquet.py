# scripts permettant de récupérer et convertir des données json provenant 
# d'une api rest et de la convertir au format désiré (ici parquet par ex)
# reste à voir si il est possible de se passer du csv / gpkg temporaire
# en utilisant la df/gdf comme input de gdal/ogr

import requests
import json
import pandas as pd
import os
from osgeo import gdal

#osecour #maisquelenfer #toutcapourca 

#dir = dossier de récupération des données

dir = r''

# payload est un dictionnaire qui contient les paramètres de la requête get

payload = {}

# uri = url de l'api rest

uri = ''

r = requests.get(uri, params=payload)
json_object = json.loads(r.text)
df = pd.json_normalize(json_object)
df.to_csv(dir+r'\test.csv')
gdal.VectorTranslate(dir+r'\test.parquet', dir+r'\test.csv', format='Parquet')
os.remove(dir+r'\test.csv')
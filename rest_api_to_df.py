# -*- coding:Utf8 -*-

# scripts permettant de récupérer et convertir des données json provenant 
# d'une api rest et de les transposer dans une dataframe pandas

import requests
import json
import pandas as pd

#osecour #maisquelenfer #toutcapourca 

def rest_to_df(uri,token,headers,nom_return,payload):
    if headers == 1:
        headers = {'Authorization': f'Bearer {token}'}
        r = requests.get(uri, params=payload, headers=headers)
    else:
        payload['apikey'] = token
        r = requests.get(uri, params=payload)
    json_object = json.loads(r.text)
    if headers == 1:
        json_object = json_object[nom_return]
    else:
        pass
    df = pd.json_normalize(json_object)
    return df

# uri = url de l'api rest
uri = ''
# token/clef d'Autorisation'
token = ''
# Le token est il donné dans les headers ou les paramètres ?
headers = '' # 0 si token en paramètres (apikey=), 1 si en headers
# Nom de la clef contenants les resultats si les headers sont retournés
nom_return = ''
# payload est un dictionnaire qui contient les paramètres de la requête get
payload = {'clef':'valeur'}

df = rest_to_df(uri, token, headers, nom_return, payload)

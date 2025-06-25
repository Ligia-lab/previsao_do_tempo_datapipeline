import os
from os.path import join
import pandas as pd
from datetime import datetime, timedelta


#intervalo de datas
data_inicio = datetime.today()
data_fim = data_inicio + timedelta(days=7)

#formatação das datas sem hora
data_inicio = data_inicio.strftime('%Y-%m-%d')
data_fim = data_fim.strftime('%Y-%m-%d')

city = 'Boston'
key = 'E95K7U8AMXUC9LQFSYNB7RY5V'

#o join é usado porque a url foi dividida em duas partes
URL = join('https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/',
           f'{city}/{data_inicio}/{data_fim}?unitGroup=metric&include=days&key={key}&contentType=csv')

dados = pd.read_csv(URL)
print(dados.head())
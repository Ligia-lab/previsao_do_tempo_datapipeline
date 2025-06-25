from airflow import DAG
from airflow.macros import ds_add
from airflow.providers.standard.operators.bash import BashOperator
from airflow.providers.standard.operators.python import PythonOperator
import pendulum
from os.path import join
import pandas as pd



with DAG(
    'dados_climaticos',
    start_date=pendulum.datetime(2025, 5, 26, tz="UTC"),
    schedule='0 0 * * 1' # executar toda segunda feira
) as dag:
    
    tarefa_1 = BashOperator(
        task_id = 'cria_pasta',
        bash_command = 'mkdir -p "/home/ligia/Documents/ALURA/Engenharia/previsao_do_tempo_datapipeline/semana={{data_interval_end | ds}}/"'
        )
    print('pasta criada!!!!!!!!!!!!!!!!')
    
    
    def extrai_dados(data_interval_end):
        
        city = 'Boston'
        key = 'E95K7U8AMXUC9LQFSYNB7RY5V'

        #o join é usado porque a url foi dividida em duas partes
        URL = join('https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/',
                f'{city}/{data_interval_end}/{ds_add(data_interval_end, 7)}?unitGroup=metric&include=days&key={key}&contentType=csv')

        dados = pd.read_csv(URL)
        print(dados.head())

        #pasta onde os arquivos serão salvos
        file_path = f'/home/ligia/Documents/ALURA/Engenharia/previsao_do_tempo_datapipeline/semana={data_interval_end}/'
    

        #salvando os arquivos
        dados.to_csv(file_path + 'dados_brutos.csv')
        dados[['datetime', 'tempmin', 'temp', 'tempmax']].to_csv(file_path + 'temperaturas.csv')
        dados[['datetime', 'description', 'icon']].to_csv(file_path + 'condicoes.csv')
        print('executado????????????????????????????????????????')


    tarefa_2 = PythonOperator(
        task_id = 'extrair_dados',
        python_callable = extrai_dados,
        op_kwargs = {'data_interval_end' : '{{data_interval_end.strftime("%Y-%m-%d")}}'}
    )  
     

    tarefa_1 >> tarefa_2
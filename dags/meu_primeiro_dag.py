from airflow.models import DAG
import pendulum
from airflow.providers.standard.operators.empty import EmptyOperator
from airflow.providers.standard.operators.bash import BashOperator


with DAG(
    'meu_primeiro_dag',
    start_date=pendulum.today('UTC').add(days=-1),
    schedule='@daily'
) as dag:
    
    tarefa_1 = EmptyOperator(task_id = 'tarefa_1')
    tarefa_2 = EmptyOperator(task_id = 'tarefa_2')
    tarefa_3 = EmptyOperator(task_id = 'tarefa_3')
    tarefa_4 = BashOperator(
        task_id = 'cria_pasta',
        bash_command = 'mkdir -p "/home/ligia/Documents/ALURA/Engenharia/previsao_do_tempo_datapipeline/pasta={{data_interval_end | ds}}/"'
        )
    
    tarefa_1 >> [tarefa_2, tarefa_3]
    tarefa_3 >> tarefa_4



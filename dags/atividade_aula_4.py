from airflow import DAG
import pendulum
from airflow.providers.standard.operators.python import PythonOperator

with DAG(
    "atividade_aula_4",
    start_date=pendulum.today('UTC').add(days=-1),
    schedule='@daily'
) as dag:

    def cumprimentos():
        print("Boas-vindas ao Airflow!")

    tarefa = PythonOperator(
        task_id='cumprimentos',
        python_callable=cumprimentos
    )
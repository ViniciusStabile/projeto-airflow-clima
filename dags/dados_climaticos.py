from airflow import DAG
import pendulum
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from airflow.macros import ds_add
from os.path import join
import pandas as pd


with DAG(
        "dados_climaticos",
        start_date=pendulum.datetime(2025, 2, 1, tz="UTC"),
        schedule_interval='0 0 * * 1', # executar toda segunda feira
) as dag:
    
    tarefa_1 = BashOperator(
            task_id = 'cria_pasta',
            bash_command = 'mkdir -p "/home/vinicius/Documents/airflowalura/semana={{data_interval_end.strftime("%Y-%m-%d")}}"'
            )
    
    def extrai_dados(data_interval_end):
        city = 'Boston'
        key = 'WMPF47NUCXNDZ4EEW4DRUZL26'

        url = URL = join('https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/',
                    f'{city}/{data_interval_end}/{ds_Add(data_interval_end,7)}?unitGroup=metric&include=days&key={key}&contentType=csv')

        df = pd.read_csv(url)

        file_path = f"/home/vinicius/Documents/airflowalura/semana={data_interval_end}/"

        df.to_csv(file_path + "dados_brutos.csv")
        df[['datetime', 'tempmin', 'temp', 'tempmax']].to_csv(file_path + 'temperaturas.csv')
        df[['datetime', 'description', 'icon']].to_csv(file_path + 'condicoes.csv')



    tarefa_2 = PythonOperator(

        task_id = 'extrai_dados',
        python_callable = extrai_dados,
        op_kwargs = {'data_interval_end': '{{data_interval_end.strftime("%Y-%m-%d")}}'}

    )


    tarefa_1 >> tarefa_2
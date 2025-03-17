# Projeto Airflow: Coleta de Dados Climáticos

Este projeto é uma DAG do Apache Airflow que coleta dados climáticos de uma cidade específica usando a API VisualCrossing. A DAG é programada para ser executada toda segunda-feira e realiza o seguinte:

1. Cria uma pasta com a data da semana de execução.
2. Extrai dados climáticos de uma cidade (Boston, neste exemplo) e salva três arquivos CSV:
   - `dados_brutos.csv`: Dados completos do clima.
   - `temperaturas.csv`: Dados das temperaturas mínima, média e máxima.
   - `condicoes.csv`: Dados sobre as condições climáticas (descrição e ícone).

## Estrutura do Código

O projeto é composto por uma única DAG com as seguintes tarefas:

- **Tarefa 1 - Criação de Pasta (`cria_pasta`)**:
  Utiliza o `BashOperator` para criar uma pasta na estrutura de diretórios `/home/vinicius/Documents/airflowalura/semana={data}`, onde `data` é a data da execução da DAG.

- **Tarefa 2 - Extração de Dados Climáticos (`extrai_dados`)**:
  Utiliza o `PythonOperator` para extrair dados climáticos da cidade de Boston a partir da API VisualCrossing e salvar os dados em três arquivos CSV distintos na pasta criada na tarefa anterior.



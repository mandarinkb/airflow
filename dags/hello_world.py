from datetime import datetime
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator
from airflow.operators.bash_operator import BashOperator

def print_hello():
    return 'Hello world from first Airflow DAG!'

dag = DAG('ahello_world', description='Hello World DAG',
          schedule_interval='0/2 * * * *',
          start_date=datetime(2017, 3, 20), catchup=False)

# hello_operator = PythonOperator(task_id='hello_task', python_callable=print_hello, dag=dag)

# hello_operator
bash_task = BashOperator(task_id='bash_task_1',
                         bash_command="echo 'Hello Airflow!'",
                         dag=dag)
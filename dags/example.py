from datetime import datetime
from airflow import DAG
from airflow.operators.bash_operator import BashOperator


dag = DAG('run_job', description='Hello World DAG',
          schedule_interval='0/1 * * * *',
          start_date=datetime(2017, 3, 20), catchup=False)

bash_task = BashOperator(task_id='bash_task_1',
                        #  bash_command="scripts/ex.sh",
                        bash_command="cd ${AIRFLOW_HOME}/dags/job; ./go-batch -job=makro",
                         dag=dag)
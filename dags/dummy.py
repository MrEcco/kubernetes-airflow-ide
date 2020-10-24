# Demonstrates what DummyOperator doesnt spawn any pods
from datetime import datetime

from airflow.models import DAG
from airflow.operators.dummy_operator import DummyOperator

args = {
    'owner': 'Airflow',
    'start_date': datetime(2020, 1, 1)
}

dag = DAG(
    dag_id='dummy',
    default_args=args,
    schedule_interval=None,
    tags=['test']
)

t1 = DummyOperator(
    task_id = 't1',
    dag = dag,
)

t2 = DummyOperator(
    task_id = 't2',
    dag = dag,
)

t1 >> t2

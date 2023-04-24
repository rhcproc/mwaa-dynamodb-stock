# test_dag.py
# This code borrows heavily from https://airflow.apache.org/docs/apache-airflow/stable/tutorial.html
from airflow.operators.python import PythonOperator
from handlers.task1 import task1_handler
from airflow import DAG
from datetime import timedelta
import datetime as dt
import logging

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email': ['rhcproc@gmail.com'],
    'email_on_failure': True,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# start_date is current time minus 15 minutes
dag = DAG(
    'simple_demo_v0.0.8',
    default_args=default_args,
    description='A simple DAG with a few Python tasks.',
    schedule=timedelta(minutes=15),
    # start_date=today('Asia/Seoul'),
    start_date=dt.datetime.today() - dt.timedelta(minutes=15),
    tags=['example']
)


def log_context(**kwargs):
    logging.info("Test - log_context")
    for key, value in kwargs.items():
        logging.info(f"Context key {key} = {value}")


def compute_product(a, b):
    logging.info(f"Inputs: a={a}, b={b}")
    if a is None or b is None:
        return None
    return a * b + 1


# OPERATORS
t1 = PythonOperator(
    task_id="task1",
    python_callable=task1_handler,
    dag=dag
)
t2 = PythonOperator(
    task_id="task2",
    python_callable=compute_product,
    op_kwargs={'a': 3, 'b': 5},
    dag=dag
)

t1 >> t2

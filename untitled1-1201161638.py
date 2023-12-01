from airflow.operators.bash_operator import BashOperator
from airflow import DAG
from airflow.utils.dates import days_ago

args = {
    "project_id": "untitled1-1201161638",
}

dag = DAG(
    "untitled1-1201161638",
    default_args=args,
    schedule_interval="@once",
    start_date=days_ago(1),
    description="""
Created with Elyra 3.15.0 pipeline editor using `untitled1.pipeline`.
    """,
    is_paused_upon_creation=False,
)


# Operator source: {"catalog_type": "airflow-package-catalog", "component_ref": {"airflow_package": "apache_airflow-1.10.15-py2.py3-none-any.whl", "file": "airflow/operators/bash_operator.py"}}

op_9f141664_efd9_40f5_b8fb_1764abc2dbca = BashOperator(
    task_id="BashOperator",
    bash_command="ls",
    xcom_push=True,
    env={},
    output_encoding="utf-8",
    executor_config={},
    dag=dag,
)

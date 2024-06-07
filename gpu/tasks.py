import os
from celery import Celery
from time import sleep
from celery.schedules import crontab
import pandas as pd
import os

celery = Celery(__name__)
celery.conf.broker_url = os.environ.get("CELERY_BROKER_URL")
celery.conf.result_backend = os.environ.get("CELERY_RESULT_BACKEND")

# celery.conf.task_queues = (
#     Queue('default', default_exchange, routing_key='default'),
#     Queue('videos', media_exchange, routing_key='media.video'),
#     Queue('images', media_exchange, routing_key='media.image')
# )



# CELERY_TASK_ROUTES = {
#  'app1.tasks.*': {'queue': 'queue1'},
#  'app2.tasks.*': {'queue': 'queue2'},
# }
# CELERY_BEAT_SCHEDULE = {
#     'app1_test': {
#         'task': 'app1.tasks.app1_test',
#         'schedule': 15,
#         'options': {'queue': 'queue1'}
#     },
#     'app2_test': {
#         'task': 'app2.tasks.app2_test',
#         'schedule': 15,
#         'options': {'queue': 'queue2'}
#     },

# }

@celery.task(name="process")
def process(arg: str, _):
    return arg

# @celery.task(name="process")
# def process(x: DefaultGraph):
#     pass



# @celery.task(name="manual_client")
# def manual_client(
#     path="/app/src/client_bulksearch/queries/sql/clientName.sql", index_name="client"
# ):
#     data = get_index_data(filepath=path)
#     r = index_data(data=data, index_name=index_name)
#     return True


# @celery.task(name="ingest_index_csv")
# def ingest_index_csv():
#     data = pd.read_csv("/app/src/clients.csv")
#     data = data[["ClientNumber", "ClientName"]]
#     gen = index_data(data=data, index_name="client", local=True)
#     r = [i for i in gen]
#     return True


# @celery.task(name="ingest_index_sql")
# def ingest_index_sql(filepath, index_name):
#     data = get_index_data(filepath=filepath)
#     gen = index_data(data=data, index_name=index_name)
#     r = [i for i in gen]
#     return True


# @celery.task(name="ingest_index_df")
# def ingest_index_df(path="/app/src/clients.csv", index_name="client"):
#     # r = os.getcwd()
#     data = pd.read_csv(path)
#     data = data[["ClientName", "ClientNumber"]]
#     r = index_data(data=data, index_name=index_name, dataframe=True)
#     return True


# celery.conf.beat_schedule = {
#     'ingest_index_sql_periodically': {
#         'task': 'ingest_index_sql',
#         'schedule': crontab(minute=0, hour=0),
#         'args': ("/app/src/client_bulksearch/queries/sql/clientName.sql", "client")
#     },
# }

# @celery.on_after_configure.connect
# def setup_periodic_tasks(sender, **kwargs):
#     sender.add_periodic_task(
#         crontab(minute=0, hour=0),
#         ingest_index_sql.s(
#             "/app/src/client_bulksearch/queries/sql/clientName.sql", "client"
#         ),
#     )
#     # sender.add_periodic_task(5.0, test_task.s("hello"))

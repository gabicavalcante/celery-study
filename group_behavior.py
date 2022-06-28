import random
import time 

from os import environ
from celery import Celery

# group
# The group primitive is a signature that takes a list of tasks that should be applied in parallel.
from celery import group

environ.setdefault('CELERY_CONFIG_MODULE', 'celery_config')

app = Celery()
app.config_from_envvar('CELERY_CONFIG_MODULE')

@app.task
def final_sub_task():
    print("Final sub task!")

@app.task
def sub_task(t):
    print(t)
    time.sleep(t)

@app.task
def task(t):
    print(t)
    time.sleep(t)

    jobs = group(*[sub_task.s(t*5) for t in range(2)])

    workflow = jobs | final_sub_task.si()
    workflow()

    print(f"Called second group!")

@app.task
def final_task():
    print("Final task!")

@app.task
def run_group():
    jobs = group(*[task.s(t) for t in range(10)])

    workflow = jobs | final_task.si()
    workflow()

    print(f"Called first group!")


def run():
    run_group.delay()

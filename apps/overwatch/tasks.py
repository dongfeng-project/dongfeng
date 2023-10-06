import subprocess

from celery import shared_task


@shared_task
def block_subprocess_task():
    p = subprocess.run("sleep 10 && echo 100", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    return p.stdout.decode(encoding="utf-8")

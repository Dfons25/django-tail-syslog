from celery import shared_task, current_task
from numpy import random
from scipy.fftpack import fft
from time import sleep
import time
import subprocess
import select

@shared_task
def debug_task():
    """
       Brainless number crunching just to have a substantial task:
    """
    the_progress = 0
    progress_list = []
    for the_progress in long_func():
        progress_list.append(the_progress)
        current_task.update_state(state='PROGRESS',
                                  meta={
                                  'progress': progress_list,
                                  'pct': the_progress})
    return random.random()

def long_func():
    # i = 0
    # while i < 100:
    #     yield i
    #     sleep(random.random())
    #     i += 1
    f = subprocess.Popen(['tail', '-F', '/var/log/syslog'], \
                         stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    p = select.poll()
    p.register(f.stdout)
    while True:
        if p.poll(1):
            yield f.stdout.readline().decode()
        time.sleep(1)

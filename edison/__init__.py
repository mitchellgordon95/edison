import networkx
import os
from edison.tasks import Task, is_done, run, mark_done

tasks = []


def task(func):
    new_task = Task(len(tasks), func)
    try:
        os.makedirs(new_task.name)
    except FileExistsError:
        pass
    tasks.append(new_task)
    return new_task


def reach(task):
    if not is_done(task):
        print(f"Running {task.name}")
        run(task)
        mark_done(task)
    else:
        print(f"Skipping {task.name} which was completed.")

import heapq
import time
from collections import deque
from queue import PriorityQueue, Queue

resources = []
tasks = []
Priority_queue = []
waiting_queue = []
queue = []


class Task:
    def __init__(self, name, type, execution_time):
        self.waiting_time = 0
        if type == 'x':
            self.type = 3
        if type == 'y':
            self.type = 2
        if type == 'z':
            self.type = 1
        self.name = name
        self.execution_time = execution_time

    def __str__(self):
        return self.name
    # def __lt__(self, other):
    #     return self.execution_time < other.execution_time


def check_resources(task, resources):
    if task.type == 3:
        if resources[0] > 0 and resources[1] > 0:
            return True
    elif task.type == 2:
        if resources[2] > 0 and resources[1] > 0:
            return True
    elif task.type == 1:
        if resources[0] > 0 and resources[2] > 0:
            return True
    else:
        return False


def zero_resources(resources):
    for i in resources:
        if (i != 0):
            return False
    return True


def need_resources(task, resources):
    n = 0
    if task.type == 3:
        if resources[0] > 0:
            n += 1
        if resources[1] > 0:
            n += 1
    elif task.type == 2:
        if resources[2] > 0:
            n += 1
        if resources[1] > 0:
            n += 1
    elif task.type == 1:
        if resources[0] > 0:
            n += 1
        if resources[2] > 0:
            n += 1
    return n


def allocate_resources(task, resources):
    if task.type == 3:
        resources[0] -= 1
        resources[1] -= 1
    elif task.type == 2:
        resources[2] -= 1
        resources[1] -= 1
    elif task.type == 1:
        resources[0] -= 1
        resources[2] -= 1


def release_resources(task, resources):
    if task.type == 3:
        resources[0] += 1
        resources[1] += 1
    elif task.type == 2:
        resources[2] += 1
        resources[1] += 1
    elif task.type == 1:
        resources[2] += 1
        resources[0] += 1


def add_to_waiting(task):
    waiting_queue.append(task)


def remove_from_waiting(task, resources):
    if check_resources(task, resources):
        waiting_queue.remove(task)


def show_waiting_tasks():
    for task in waiting_queue:
        print(task)


def print_status(resource, running, priority_queue, waiting_queue):
    print(f"R1: {resource[0]} R2:  {resource[1]}  R3: {resource[2]}")
    print(f"priority_queue:{[t.name for t in priority_queue]}")
    # if(running!=None):
    print(f"running:{running.name}")
    print(f"waiting_queue:{[t.name for t in waiting_queue]}")


def SJF(tasks, resources):
    running = None
    tasks.sort(key=lambda t: t.execution_time)
    while len(tasks) > 0 or running is not None:
        while running == None:
            task = tasks.pop(0)
            # task = heapq.heappop([(t.execution_time,t) for t in t])
            if check_resources(task, resources):
                allocate_resources(task, resources)
                running = task
            else:
                add_to_waiting(task)

        running.execution_time -= 1
        print_status(resources, running, tasks, waiting_queue)
        if running.execution_time == 0:
            release_resources(running, resources)
            running = None
        changed = False
        for i in range(len(waiting_queue)):
            task = waiting_queue.pop(0)
            # task = heapq.heappop(waiting_queue, key=lambda t: t.execution_time)
            if check_resources(task, resources):
                tasks.append(task)
                changed = True
            else:
                add_to_waiting(task)
        if changed:
            tasks.sort(key=lambda t: t.execution_time)

if __name__ == "__main__":
    R1 = int(input("number of resources for R1: "))
    resources.append(R1)
    R2 = int(input("number of resources for R2: "))
    resources.append(R2)
    R3 = int(input("number of resources for R3: "))
    resources.append(R3)
    print(resources)
    num_tasks = int(input("number of tasks: "))
    for i in range(num_tasks):
        task_name = input("name of task: ")
        task_type = input("type of task: ")
        task_duration = int(input("time of task: "))
        tasks.append(Task(task_name, task_type, task_duration))
    choose = input("choose the algorithm: ")
    if choose == 'SJF':
        SJF(tasks, resources)
    # elif choose == 'FCFS':
    #     # FCFS(tasks, resources)
    # if choose == 'RR':
    #     time_slice = int(input("time slice: "))
    #     # Round_Robin(tasks, resources, time_slice)
    # if choose == 'HRRN':
    #     # arrival_time = int(input("Arrival time: "))
    #     # HRRN(tasks, resources)

    # print("list of tasks:")
    # for task in tasks:
    #     print(task)

import numpy as np

print("\n---TO DO LIST (CLI)---\n")

tasks = [["1. Sample String task"], ["2. Sample string task"]]

def addTask(taskList: list,string: str):
    li = []
    li.append(string)
    taskList.append(li)
    return taskList

tasks = addTask(tasks,"3. Water the shoe")
print(tasks)

# this isnt done yet. I am going to use numpy's 2D arrays
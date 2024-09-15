import math

def calculate_estimation(a, m, b):
    E_task = (a + 4 * m + b) / 6
    SD_task = (b - a) / 6
    return E_task, SD_task

def calculate_confidence_interval(E_task, SD_task):
    E_project = sum(E_task)
    SE_project = math.sqrt(sum(SD_task**2 for SD in SD_task))
    CI_min = E_project - 2 * SE_project
    CI_max = E_project + 2 * SE_project
    return CI_min, CI_max

def get_task_estimations():
    tasks = []
    while True:
        a = float(input("Enter the optimistic estimate (a) for a task (or 'q' to finish): "))
        if a == 'q':
            break
        m = float(input("Enter the most likely estimate (m) for the task: "))
        b = float(input("Enter the pessimistic estimate (b) for the task: "))
        tasks.append((a, m, b))
    return tasks

def main():
    tasks = get_task_estimations()
    E_tasks = []
    SD_tasks = []
    for task in tasks:
        E_task, SD_task = calculate_estimation(*task)
        E_tasks.append(E_task)
        SD_tasks.append(SD_task)
    
    CI_min, CI_max = calculate_confidence_interval(E_tasks, SD_tasks)

    print("Project's 95% confidence interval:", CI_min, "...", CI_max, "points")

if __name__ == '__main__':
    main()

from functools import reduce

tasks = [
    (1, 3, 50),  
    (2, 5, 20),
    (3, 9, 100),
    (6, 8, 70),
    (8, 11, 60),
    (9, 12, 40)
]

def schedule_tasks_procedural(tasks):
    tasks.sort(key=lambda x: x[1])
    selected_tasks = []
    total_reward = 0
    last_end_time = 0

    for start, end, reward in tasks:
        if start >= last_end_time:
            selected_tasks.append((start, end, reward))
            total_reward += reward
            last_end_time = end

    return total_reward, selected_tasks

def schedule_tasks_functional(tasks):
    sorted_tasks = sorted(tasks, key=lambda x: x[1])
    schedule = reduce(
        lambda acc, task: acc if task[0] < acc[-1][1] else acc + [task],
        sorted_tasks[1:],
        [sorted_tasks[0]]
    ) if sorted_tasks else []

    total_reward = sum(map(lambda x: x[2], schedule))
    return total_reward, schedule

procedural_reward, procedural_schedule = schedule_tasks_procedural(tasks)
functional_reward, functional_schedule = schedule_tasks_functional(tasks)

print("Proceduralne podejście:")
print("Maksymalna nagroda:", procedural_reward)
print("Wybrane zadania:", procedural_schedule)

print("\nFunkcyjne podejście:")
print("Maksymalna nagroda:", functional_reward)
print("Wybrane zadania:", functional_schedule)

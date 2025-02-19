from functools import reduce

tasks = [
    (3, 50),  
    (1, 40), 
    (2, 30), 
    (5, 20)  
]

def optimize_tasks_procedural(tasks):
    """Optymalizacja zadań proceduralnie (sortowanie + pętla)"""
    sorted_tasks = sorted(tasks, key=lambda x: x[0]) 
    
    total_waiting_time = 0
    waiting_time = 0
    
    for i in range(len(sorted_tasks) - 1):
        waiting_time += sorted_tasks[i][0]
        total_waiting_time += waiting_time

    return sorted_tasks, total_waiting_time

def optimize_tasks_functional(tasks):
    """Optymalizacja zadań funkcyjnie (sorted + map + reduce)"""
    sorted_tasks = sorted(tasks, key=lambda x: x[0]) 
    
    waiting_times = list(map(lambda i: sum(t[0] for t in sorted_tasks[:i]), range(1, len(sorted_tasks))))
    total_waiting_time = reduce(lambda acc, x: acc + x, waiting_times, 0)

    return sorted_tasks, total_waiting_time


procedural_result, procedural_time = optimize_tasks_procedural(tasks)
functional_result, functional_time = optimize_tasks_functional(tasks)

print("Proceduralne podejście:")
print("Optymalna kolejność zadań:", procedural_result)
print("Całkowity czas oczekiwania:", procedural_time)

print("\nFunkcyjne podejście:")
print("Optymalna kolejność zadań:", functional_result)
print("Całkowity czas oczekiwania:", functional_time)

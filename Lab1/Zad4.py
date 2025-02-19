from functools import lru_cache

items = [
    (2, 3),  
    (3, 4), 
    (4, 5), 
    (5, 8)   
]
capacity = 8  

def knapsack_procedural(items, capacity):
    n = len(items)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        weight, value = items[i - 1]
        for w in range(capacity + 1):
            if weight > w:
                dp[i][w] = dp[i - 1][w]
            else:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weight] + value)

    selected_items = []
    w = capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected_items.append(items[i - 1])
            w -= items[i - 1][0]

    return dp[n][capacity], selected_items

@lru_cache(None)
def knapsack_functional(i, remaining_capacity):
    if i < 0 or remaining_capacity == 0:
        return 0, []

    weight, value = items[i]

    if weight > remaining_capacity:
        return knapsack_functional(i - 1, remaining_capacity)  

    without_item = knapsack_functional(i - 1, remaining_capacity)
    with_item = knapsack_functional(i - 1, remaining_capacity - weight)
    with_item = (with_item[0] + value, with_item[1] + [items[i]])

    return max(without_item, with_item, key=lambda x: x[0])

procedural_value, procedural_items = knapsack_procedural(items, capacity)
functional_value, functional_items = knapsack_functional(len(items) - 1, capacity)

print("Proceduralne podejście:")
print("Maksymalna wartość w plecaku:", procedural_value)
print("Wybrane przedmioty:", procedural_items)

print("\nFunkcyjne podejście:")
print("Maksymalna wartość w plecaku:", functional_value)
print("Wybrane przedmioty:", functional_items)

#zadanie z BFS
from collections import deque
from encodings import normalize_encoding
from turtledemo.penrose import start
from xml.dom.NodeFilter import NodeFilter


def BFS(graph, start, end):
    visited = set()
    queue = deque([start])

    while queue:
        path = queue.popleft()
        node = path[-1]

        if node == end:
            return path

        if node not in visited:
            for neighbor in graph.get[node]:
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)
            visited.add(node)
    return Node


graph = {'A': ['B', 'C', 'E'],
            'B': ['A', 'D', 'E'],
            'C': ['A', 'F'],
            'D': ['B'],
            'E': ['A', 'B', 'D'],
            'F': ['C']}

print(BFS(graph, 'A', 'C'))
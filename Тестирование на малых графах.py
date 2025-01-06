import time
from collections import deque

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append(v)
        self.graph[v].append(u)

    def bfs(self, start):
        visited = {node: False for node in self.graph}
        distance = {node: float('inf') for node in self.graph}
        parent = {node: None for node in self.graph}

        queue = deque([start])
        visited[start] = True
        distance[start] = 0

        while queue:
            current = queue.popleft()
            for neighbor in self.graph[current]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    distance[neighbor] = distance[current] + 1
                    parent[neighbor] = current
                    queue.append(neighbor)

        return distance, parent

    def get_path(self, start, end):
        distance, parent = self.bfs(start)
        path = []
        current = end
        while current is not None:
            path.append(current)
            current = parent[current]
        path.reverse()
        return path if distance[end] != float('inf') else None


# Функция для проведения теста
def run_test(graph, start_node, end_node):
    start_time = time.time()
    path = graph.get_path(start_node, end_node)
    end_time = time.time()
    
    print(f"Путь от {start_node} до {end_node}: {path}")
    print(f"Время выполнения: {end_time - start_time:.6f} секунд")
    print("-" * 50)


# 1. Тест 1: Граф с 4 вершинами (Циклический граф)
g1 = Graph()
g1.add_edge(0, 1)
g1.add_edge(1, 2)
g1.add_edge(2, 3)
g1.add_edge(3, 0)

run_test(g1, 0, 2)  # Путь от 0 до 2

# 2. Тест 2: Граф с 5 вершинами (Звезда)
g2 = Graph()
g2.add_edge(0, 1)
g2.add_edge(0, 2)
g2.add_edge(0, 3)
g2.add_edge(0, 4)

run_test(g2, 1, 4)  # Путь от 1 до 4

# 3. Тест 3: Граф с 6 вершинами (Дерево)
g3 = Graph()
g3.add_edge(0, 1)
g3.add_edge(0, 2)
g3.add_edge(1, 3)
g3.add_edge(1, 4)
g3.add_edge(2, 5)

run_test(g3, 3, 5)  # Путь от 3 до 5


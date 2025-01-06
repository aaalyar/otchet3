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

# Тест 1: Граф с двумя компонентами
g1 = Graph()
# Первая компонента
g1.add_edge(0, 1)
g1.add_edge(1, 2)
g1.add_edge(2, 3)
# Вторая компонента
g1.add_edge(5, 6)
g1.add_edge(6, 7)

run_test(g1, 0, 7)  # Путь от 0 до 7, не существует

run_test(g1, 0, 3)  # Путь от 0 до 3, существует

# Тест 2: Граф с тремя компонентами
g2 = Graph()
# Первая компонента
g2.add_edge(0, 1)
g2.add_edge(1, 2)
# Вторая компонента
g2.add_edge(3, 4)
g2.add_edge(4, 5)
# Третья компонента
g2.add_edge(6, 7)


run_test(g2, 0, 5)  # Путь от 0 до 5, не существует


run_test(g2, 3, 5)  # Путь от 3 до 5, существует

# Тест 3: Граф с четырьмя компонентами
g3 = Graph()
# Первая компонента
g3.add_edge(0, 1)
# Вторая компонента
g3.add_edge(2, 3)
# Третья компонента
g3.add_edge(4, 5)
# Четвёртая компонента
g3.add_edge(6, 7)

run_test(g3, 0, 5)  # Путь от 0 до 5, не существует


run_test(g3, 2, 3)  # Путь от 2 до 3, существует

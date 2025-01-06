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


# Тестирование на полном графе с 10 вершинами
n = 10  # Число вершин для первого графа
g = Graph()

# Добавление рёбер для полного графа
for i in range(n):
    for j in range(i + 1, n):
        g.add_edge(i, j)

run_test(g, 0, 9)  # Путь от вершины 0 до вершины 9

# Тестирование на полном графе с 15 вершинами
n = 15  # Число вершин для второго графа
g = Graph()

# Добавление рёбер для полного графа
for i in range(n):
    for j in range(i + 1, n):
        g.add_edge(i, j)

run_test(g, 0, 14)  # Путь от вершины 0 до вершины 14

# Тестирование на полном графе с 20 вершинами
n = 20  # Число вершин для третьего графа
g = Graph()

# Добавление рёбер для полного графа
for i in range(n):
    for j in range(i + 1, n):
        g.add_edge(i, j)

run_test(g, 0, 19)  # Путь от вершины 0 до вершины 19

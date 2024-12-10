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

# Пример использования
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(1, 4)
g.add_edge(2, 5)

start_node = 0
end_node = 4
path = g.get_path(start_node, end_node)
print(f"Путь от {start_node} до {end_node}: {path}")

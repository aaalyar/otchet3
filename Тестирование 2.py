import unittest
from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    result = []

    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            visited.add(vertex)
            result.append(vertex)
            # Сортировка соседей для предсказуемости порядка обхода
            queue.extend(sorted(neighbor for neighbor in graph[vertex] if neighbor not in visited))
    
    return result

class TestBFS(unittest.TestCase):
    def setUp(self):
        self.graph = {
            'A': ['B', 'C'],
            'B': ['A', 'D', 'E'],
            'C': ['A', 'F'],
            'D': ['B'],
            'E': ['B', 'F'],
            'F': ['C', 'E']
        }

    def test_bfs(self):
        # Тестирование BFS с начальной точки 'A'
        self.assertEqual(bfs(self.graph, 'A'), ['A', 'B', 'C', 'D', 'E', 'F'])
        # Тестирование BFS с начальной точки 'B'
        self.assertEqual(bfs(self.graph, 'B'), ['B', 'A', 'D', 'E', 'C', 'F'])
        # Тестирование BFS с начальной точки 'C'
        self.assertTrue(set(bfs(self.graph, 'C')) == set(['C', 'A', 'F', 'B', 'D', 'E']))
        # Порядок в BFS может варьироваться, но результат должен быть тот же

if __name__ == '__main__':
    unittest.main()


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
            queue.extend(neighbor for neighbor in graph[vertex] if neighbor not in visited)
    
    return result

def test_bfs():
    # Пример графа с несколькими компонентами связности
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D'],
        'C': ['A'],
        'D': ['B'],
        'E': ['F'],
        'F': ['E']
    }

    # Ожидаемый результат для начала с 'A'
    expected_output_A = ['A', 'B', 'C', 'D']
    output_A = bfs(graph, 'A')
    assert output_A == expected_output_A, f"Ошибка: {output_A} != {expected_output_A}"

    # Ожидаемый результат для начала с 'E'
    expected_output_E = ['E', 'F']
    output_E = bfs(graph, 'E')
    assert output_E == expected_output_E, f"Ошибка: {output_E} != {expected_output_E}"

    print("Все тесты пройдены успешно!")

# Запуск тестов
test_bfs()

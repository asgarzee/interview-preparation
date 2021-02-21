from collections import deque
from collections import OrderedDict


def bfs(graph, start_node):
    queue = deque([start_node])
    visited = OrderedDict({start_node: True})
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if i not in visited:
                queue.append(i)
                visited[i] = True
    return list(visited.keys())


def dfs(graph, start_node, visited=[]):
    if start_node not in visited:
        visited.append(start_node)
        for i in graph[start_node]:
            dfs(graph, i, visited)
    return visited


if __name__ == '__main__':
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'D'],
        'D': ['B', 'C', 'E'],
        'E': ['B', 'D']
    }

    print(bfs(graph, 'A'))

    print(dfs(graph, 'A'))  # A,B,D,C, E

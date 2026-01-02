def bfs(graph, start):
    visited = set()
    queue = [start]
    visited.add(start)

    while queue:
        vertex = queue.pop(0)
        print(vertex, end=" ")

        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return queue

graph = {
    'A': ['B','D','E'],
    'B': ['C','E'],
    'C':['F'],
    'D':[],
    'E':['B','F'],
    'F': ['E','C']
}
bfs(graph,'A')
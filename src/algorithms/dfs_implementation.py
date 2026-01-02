def dfs(graph, start):
    visited = set()
    stack = [start]

    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            print(vertex, end=" ")
            visited.add(vertex)

            for neighbor in reversed(graph[vertex]):
                if neighbor not in visited:
                    stack.append(neighbor)

graph = {
    'A': ['B','D','E'],
    'B': ['C','E'],
    'C':[],
    'D':[],
    'E':['B','F'],
    'F': ['E']
}

dfs(graph,'A')

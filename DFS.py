#Algoritmo DFS

import json

def dfs_recursive(graph, source, visited=[]):
    if source not in visited:
        visited.append(source)

        if source not in graph:
            # leaf node, backtracking
            return visited

        for neighbour in graph[source]:
            visited = dfs_recursive(graph, neighbour, visited)

    return visited

if __name__ == "__main__":
    with open("GrafAgendarCita.json", "r") as f:
        graph = json.load(f)
    print(dfs_recursive(graph, "5"))
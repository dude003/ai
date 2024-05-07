from collections import deque

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end=' ')

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)

    while queue:
        node = queue.popleft()
        print(node, end=' ')

        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)

def main():
    graph = {}
    n = int(input("Enter the number of Nodes: "))
    for i in range(n):
        node = input(f"Enter node {i + 1}: ")
        neighbors = input(f"Enter Neigbours of {node} separated by space: ").split()
        graph[node] = neighbors

    start_node = input("Enter the start node: ")

    print('DFS Path = ', end=" ")
    dfs(graph, start_node)

    print('\nBFS Path = ', end=" ")
    bfs(graph, start_node)

main()
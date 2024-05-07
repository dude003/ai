def a_star(start_node, stop_node, graph_nodes, heuristic_dist):
    open_set = set([start_node])
    closed_set = set()
    g = {start_node: 0}
    parents = {start_node: start_node}

    while open_set:
        current_node = min(open_set, key=lambda x: g[x] + heuristic_dist[x])

        if current_node == stop_node:
            path = []
            while current_node != start_node:
                path.append(current_node)
                current_node = parents[current_node]
            path.append(start_node)
            path.reverse()
            print('Path found:', path)
            return path

        open_set.remove(current_node)
        closed_set.add(current_node)

        for neighbor, weight in graph_nodes.get(current_node, []):
            if neighbor in closed_set:
                continue

            tentative_g = g[current_node] + weight
            if neighbor not in open_set or tentative_g < g[neighbor]:
                g[neighbor] = tentative_g
                parents[neighbor] = current_node
                open_set.add(neighbor)

    print('Path does not exist!')
    return None

def get_user_input():
    start_node = input("Enter start node: ").strip()
    stop_node = input("Enter stop node: ").strip()

    graph_nodes = {}
    while True:
        node = input("Enter node or press Enter to stop adding nodes: ").strip()
        if not node:
            break
        neighbors = []
        while True:
            neighbor = input(f"Enter neighbor node for {node} (or press Enter to finish): ").strip()
            if not neighbor:
                break
            weight = float(input(f"Enter weight for the edge from {node} to {neighbor}: ").strip())
            neighbors.append((neighbor, weight))
        graph_nodes[node] = neighbors

    heuristic_dist = {}
    while True:
        node = input("Enter node for heuristic or press Enter to finish: ").strip()
        if not node:
            break
        dist = float(input(f"Enter heuristic distance for node {node}: ").strip())
        heuristic_dist[node] = dist

    return start_node, stop_node, graph_nodes, heuristic_dist

if __name__ == "__main__":
    start_node, stop_node, graph_nodes, heuristic_dist = get_user_input()
    a_star(start_node, stop_node, graph_nodes, heuristic_dist)

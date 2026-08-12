import heapq

def greedy_best_first_search(graph, heuristic, start, goal):
    open_list = []
    heapq.heappush(open_list, (heuristic[start], start))

    visited = set()
    parent = {start: None}

    while open_list:
        h, current = heapq.heappop(open_list)

        if current in visited:
            continue

        visited.add(current)
        print("Expanded:", current, "h =", h)

        if current == goal:
            path = []
            while current is not None:
                path.append(current)
                current = parent[current]
            return path[::-1]

        for neighbor in graph[current]:
            if neighbor not in visited:
                parent[neighbor] = current
                heapq.heappush(
                    open_list,
                    (heuristic[neighbor], neighbor)
                )

    return None


# Graph
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['G'],
    'F': ['G'],
    'G': []
}

# Heuristic values
heuristic = {
    'A': 6,
    'B': 4,
    'C': 5,
    'D': 7,
    'E': 2,
    'F': 3,
    'G': 0
}

start = 'A'
goal = 'G'

path = greedy_best_first_search(graph, heuristic, start, goal)

print("\nPath:", " -> ".join(path))

from queue import PriorityQueue

graph = {
    'A': [('B', 1), ('C', 1)],
    'B': [('D', 1), ('E', 1)],
    'C': [('F', 1)],
    'D': [],
    'E': [('G', 1)],
    'F': [('G', 1)],
    'G': []
}

heuristic = {
    'A': 6,
    'B': 4,
    'C': 3,
    'D': 5,
    'E': 2,
    'F': 1,
    'G': 0
}

def greedy_best_first(start, goal):
    pq = PriorityQueue()
    pq.put((heuristic[start], start))

    visited = set()
    parent = {}

    while not pq.empty():
        h, node = pq.get()

        if node in visited:
            continue

        visited.add(node)

        if node == goal:
            path = []
            while node:
                path.append(node)
                node = parent.get(node)
            return path[::-1]

        for neighbor, cost in graph[node]:
            if neighbor not in visited:
                parent[neighbor] = node
                pq.put((heuristic[neighbor], neighbor))

    return None

start = input("Enter Start Node: ")
goal = input("Enter Goal Node: ")

path = greedy_best_first(start, goal)

print("Path:", " -> ".join(path))

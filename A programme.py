from queue import PriorityQueue

graph = {
    'A': [('B', 2), ('C', 4)],
    'B': [('D', 3), ('E', 1)],
    'C': [('F', 5)],
    'D': [('G', 2)],
    'E': [('G', 4)],
    'F': [('G', 1)],
    'G': []
}

heuristic = {
    'A': 7,
    'B': 6,
    'C': 4,
    'D': 2,
    'E': 3,
    'F': 1,
    'G': 0
}

def astar(start, goal):
    pq = PriorityQueue()
    pq.put((heuristic[start], 0, start))

    parent = {}
    cost = {start: 0}

    while not pq.empty():
        f, g, node = pq.get()

        if node == goal:
            path = []
            while node:
                path.append(node)
                node = parent.get(node)
            return path[::-1], g

        for neighbor, weight in graph[node]:
            new_cost = g + weight

            if neighbor not in cost or new_cost < cost[neighbor]:
                cost[neighbor] = new_cost
                parent[neighbor] = node
                priority = new_cost + heuristic[neighbor]
                pq.put((priority, new_cost, neighbor))

    return None, 0

start = input("Enter Start Node: ")
goal = input("Enter Goal Node: ")

path, cost = astar(start, goal)

print("Shortest Path:", " -> ".join(path))
print("Total Cost:", cost)

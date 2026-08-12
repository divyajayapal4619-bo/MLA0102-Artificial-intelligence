import heapq

def a_star(graph, heuristic, start, goal):

    open_list = []

    # (f, g, node)
    heapq.heappush(open_list, (heuristic[start], 0, start))

    g_cost = {start: 0}
    parent = {start: None}
    visited = set()

    while open_list:

        f, g, current = heapq.heappop(open_list)

        if current in visited:
            continue

        visited.add(current)

        print("Expanded:", current,
              "g =", g,
              "h =", heuristic[current],
              "f =", f)

        if current == goal:

            path = []

            while current is not None:
                path.append(current)
                current = parent[current]

            return path[::-1], g

        for neighbor, cost in graph[current]:

            new_g = g + cost

            if neighbor not in g_cost or new_g < g_cost[neighbor]:

                g_cost[neighbor] = new_g
                parent[neighbor] = current

                new_f = new_g + heuristic[neighbor]

                heapq.heappush(
                    open_list,
                    (new_f, new_g, neighbor)
                )

    return None, float("inf")


# Weighted graph
graph = {
    'A': [('B', 2), ('C', 4)],
    'B': [('D', 3), ('E', 2)],
    'C': [('F', 3)],
    'D': [('G', 4)],
    'E': [('G', 3)],
    'F': [('G', 2)],
    'G': []
}

# Heuristic values
heuristic = {
    'A': 6,
    'B': 5,
    'C': 4,
    'D': 4,
    'E': 2,
    'F': 2,
    'G': 0
}

start = 'A'
goal = 'G'

path, cost = a_star(graph, heuristic, start, goal)

print("\nOptimal Path:", " -> ".join(path))
print("Total Cost:", cost)

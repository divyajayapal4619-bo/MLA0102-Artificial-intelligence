# Online Search Agent for a Warehouse Robot

warehouse = [
    ['S', '.', '.', '.', '.'],
    ['.', '#', '#', '.', '.'],
    ['.', '.', '.', '.', '.'],
    ['.', '#', '.', '#', '.'],
    ['.', '.', '.', '.', 'G']
]

rows = len(warehouse)
cols = len(warehouse[0])


def show_warehouse():

    for row in warehouse:
        print(" ".join(row))

    print()


def get_neighbors(position):

    r, c = position

    directions = [
        (-1, 0),   # Up
        (1, 0),    # Down
        (0, -1),   # Left
        (0, 1)     # Right
    ]

    neighbors = []

    for dr, dc in directions:

        nr = r + dr
        nc = c + dc

        if 0 <= nr < rows and 0 <= nc < cols:

            if warehouse[nr][nc] != '#':
                neighbors.append((nr, nc))

    return neighbors


def bfs(start, goal):

    queue = [start]
    parent = {start: None}

    while queue:

        current = queue.pop(0)

        if current == goal:

            path = []

            while current is not None:
                path.append(current)
                current = parent[current]

            return path[::-1]

        for neighbor in get_neighbors(current):

            if neighbor not in parent:

                parent[neighbor] = current
                queue.append(neighbor)

    return None


# Start and goal
start = (0, 0)
goal = (4, 4)

print("Initial Warehouse:")
show_warehouse()

path = bfs(start, goal)

print("Initial Path:")
print(path)


# Dynamic obstacle appears
new_obstacle = (2, 3)

print("\nObstacle appeared at:", new_obstacle)

warehouse[new_obstacle[0]][new_obstacle[1]] = '#'

print("\nUpdated Warehouse:")
show_warehouse()


# Robot replans
new_path = bfs(start, goal)

print("New Path after replanning:")
print(new_path)

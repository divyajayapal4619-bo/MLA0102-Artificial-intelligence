cave = {}

n = int(input("Enter number of caves: "))

for i in range(n):
    cave_name = input("Cave: ")
    path = input("Connected caves: ").split()
    cave[cave_name] = path

start = input("Starting cave: ")

visited = []

def dfs(node):
    visited.append(node)
    print("Drone entered:", node)

    for x in cave.get(node, []):
        if x not in visited:
            dfs(x)

    print("Backtracking from:", node)

print("\n Rescue Drone Exploration")
dfs(start)

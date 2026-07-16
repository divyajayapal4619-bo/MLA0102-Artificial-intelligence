from queue import PriorityQueue

graph = {}

n = int(input("Enter number of edges: "))

for i in range(n):
    u = input("From: ")
    v = input("To: ")
    c = int(input("Cost: "))

    if u not in graph:
        graph[u] = {}
    graph[u][v] = c

    if v not in graph:
        graph[v] = {}

start = input("Enter Source: ")
goal = input("Enter Destination: ")

pq = PriorityQueue()
pq.put((0, start, [start]))
visited = []

while not pq.empty():
    cost, node, path = pq.get()

    if node == goal:
        print("\nLeast Cost Path:", " -> ".join(path))
        print("Minimum Cost:", cost)
        break

    if node not in visited:
        visited.append(node)

        for nxt in graph[node]:
            if nxt not in visited:
                pq.put((cost + graph[node][nxt], nxt, path + [nxt]))

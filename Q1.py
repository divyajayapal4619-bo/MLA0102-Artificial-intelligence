from collections import deque

maze = [
    [0,0,1,0,0],
    [1,0,1,0,1],
    [0,0,0,0,0],
    [0,1,1,1,0],
    [0,0,0,1,0]
]

start = (0,0)
goal = (4,4)

rows, cols = len(maze), len(maze[0])
queue = deque([(start, [start])])
visited = set([start])

while queue:
    (x,y), path = queue.popleft()
    if (x,y) == goal:
        print("Shortest Path:", path)
        print("Steps:", len(path)-1)
        break

    for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
        nx, ny = x+dx, y+dy
        if 0 <= nx < rows and 0 <= ny < cols:
            if maze[nx][ny] == 0 and (nx,ny) not in visited:
                visited.add((nx,ny))
                queue.append(((nx,ny), path+[(nx,ny)]))

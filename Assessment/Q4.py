import random

columns = list(range(7))

print("AI chooses column:", random.choice(columns))
from queue import PriorityQueue

goal = (1,2,3,4,5,6,7,8,0)

start = (1,2,3,
         4,0,6,
         7,5,8)

def heuristic(state):
    return sum(state[i] != goal[i] and state[i] != 0 for i in range(9))

pq = PriorityQueue()
pq.put((heuristic(start),0,start,[]))
visited = set()

while not pq.empty():
    f,g,state,path = pq.get()

    if state == goal:
        print("Solved!")
        print("Moves:", path)
        break

    if state in visited:
        continue

    visited.add(state)

    zero = state.index(0)
    x,y = divmod(zero,3)

    for dx,dy,move in [(-1,0,'Up'),(1,0,'Down'),(0,-1,'Left'),(0,1,'Right')]:
        nx,ny = x+dx,y+dy
        if 0<=nx<3 and 0<=ny<3:
            nz = nx*3+ny
            lst = list(state)
            lst[zero],lst[nz] = lst[nz],lst[zero]
            new = tuple(lst)
            pq.put((g+1+heuristic(new),g+1,new,path+[move]))

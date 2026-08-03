from collections import deque

capacity1 = 11
capacity2 = 9
target = 8

visited = set()
queue = deque([((0,0), [])])

while queue:
    (a,b), path = queue.popleft()

    if a == target or b == target:
        print("Solution:")
        for step in path:
            print(step)
        print("Final:", (a,b))
        break

    if (a,b) in visited:
        continue

    visited.add((a,b))

    next_states = [
        ((capacity1,b),"Fill 11L"),
        ((a,capacity2),"Fill 9L"),
        ((0,b),"Empty 11L"),
        ((a,0),"Empty 9L"),
    ]

    transfer = min(a, capacity2-b)
    next_states.append(((a-transfer,b+transfer),"11->9"))

    transfer = min(b, capacity1-a)
    next_states.append(((a+transfer,b-transfer),"9->11"))

    for state, action in next_states:
        if state not in visited:
            queue.append((state, path+[action]))

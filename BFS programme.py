from collections import deque

rooms = {}
n = int(input("Enter number of rooms: "))

for i in range(n):
    room = input("Room: ")
    connected = input("Connected rooms: ").split()
    rooms[room] = connected

start = input("Starting room: ")

visited = set()
queue = deque([start])

print("\n🤖 Robot Path")

level = 0
while queue:
    size = len(queue)
    print("Level", level, ":", end=" ")

    for i in range(size):
        room = queue.popleft()
        if room not in visited:
            visited.add(room)
            print(room, end=" ")

            for x in rooms.get(room, []):
                if x not in visited:
                    queue.append(x)

    print()
    level += 1

print("\nAll rooms visited successfully!")

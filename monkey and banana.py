# Monkey and Banana Problem

robot = "A"
box = "B"
banana = "C"
has_banana = False

print("Initial State")
print("Robot Position:", robot)
print("Box Position:", box)
print("Banana Position:", banana)
print()

if robot != box:
    print("Action 1: Move to the box")
    robot = box

if box != banana:
    print("Action 2: Push the box under the banana")
    box = banana
    robot = banana

print("Action 3: Climb the box")

print("Action 4: Pick the banana")
has_banana = True

if has_banana:
    print("\nGoal Achieved! Robot has obtained the banana.")

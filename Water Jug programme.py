jug1 = int(input("Enter capacity of Jug 1: "))
jug2 = int(input("Enter capacity of Jug 2: "))
goal = int(input("Enter goal amount: "))

print("\nSequence of Operations")

print("(0,0)")
print(f"Fill Jug1 -> ({jug1},0)")
print(f"Pour Jug1 to Jug2 -> (0,{jug1})")
print(f"Fill Jug1 again -> ({jug1},{jug1})")

remaining = jug2 - jug1
answer = jug1 - remaining

print(f"Pour until Jug2 is full -> ({answer},{jug2})")

if answer == goal:
    print("\nGoal Reached:", goal, "Litres")
else:
    print("\nGoal not reached with this sequence.")

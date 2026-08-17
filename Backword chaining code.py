facts = {
    "fly",
    "tough"
}

rules = {
    "furry": ["fly"],
    "fly": ["furry"],
    "rest": ["furry", "tough"]
}


def backward_chaining(goal, facts, rules, visited=None):
    if visited is None:
        visited = set()

    if goal in facts:
        return True

    if goal in visited:
        return False

    visited.add(goal)

    if goal not in rules:
        return False

    conditions = rules[goal]

    for condition in conditions:
        if not backward_chaining(condition, facts, rules, visited):
            return False

    return True


print("BACKWARD CHAINING")
print("------------------")

goal = input("Enter goal: ").lower()

if backward_chaining(goal, facts, rules):
    print("Goal", goal, "can be proved from facts.")
else:
    print("Goal", goal, "cannot be proved from given facts.")

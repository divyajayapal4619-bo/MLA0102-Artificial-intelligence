facts = {
    "fly",
    "cough"
}

rules = {
    "furry": ["fly", "cough"],
    "rest": ["furry"],
    "doctor_visit": ["furry", "rest"]
}


def forward_chaining(facts, rules):

    facts = set(facts)
    changed = True

    while changed:
        changed = False

        for conclusion, conditions in rules.items():

            if all(condition in facts for condition in conditions):
                if conclusion not in facts:
                    facts.add(conclusion)
                    changed = True

    return facts


print("FORWARD CHAINING")
print("-----------------")

final_facts = forward_chaining(facts, rules)

print("Initial facts:")
for fact in facts:
    print("-", fact)

print("\nFinal facts:")
for fact in final_facts:
    print("-", fact)

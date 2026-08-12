# CSP: Examination Timetable
# MRV + Forward Checking

subjects = {
    "AI": ["9AM", "11AM"],
    "DBMS": ["9AM", "11AM"],
    "OS": ["11AM", "2PM"],
    "CN": ["9AM", "2PM"],
    "Maths": ["9AM", "11AM", "2PM"]
}

# Conflicting subjects
conflicts = {
    "AI": {"DBMS", "OS"},
    "DBMS": {"AI", "CN"},
    "OS": {"AI", "Maths"},
    "CN": {"DBMS", "Maths"},
    "Maths": {"OS", "CN"}
}


def is_consistent(subject, value, assignment):

    for other in conflicts[subject]:

        if other in assignment:
            if assignment[other] == value:
                return False

    return True


# MRV: choose subject with smallest remaining domain
def select_mrv(domains, assignment):

    unassigned = [
        s for s in domains
        if s not in assignment
    ]

    return min(unassigned, key=lambda s: len(domains[s]))


# Forward Checking
def forward_check(subject, value, domains, assignment):

    new_domains = {
        s: list(domains[s])
        for s in domains
    }

    new_domains[subject] = [value]

    for other in conflicts[subject]:

        if other not in assignment:
            if value in new_domains[other]:
                new_domains[other].remove(value)

                if len(new_domains[other]) == 0:
                    return None

    return new_domains


def backtracking(assignment, domains):

    if len(assignment) == len(subjects):
        return assignment

    subject = select_mrv(domains, assignment)

    print("Selected using MRV:", subject)

    for value in domains[subject]:

        if is_consistent(subject, value, assignment):

            print("Trying:", subject, "=", value)

            new_domains = forward_check(
                subject,
                value,
                domains,
                assignment
            )

            if new_domains is not None:

                assignment[subject] = value

                result = backtracking(
                    assignment,
                    new_domains
                )

                if result is not None:
                    return result

                del assignment[subject]

    return None


solution = backtracking({}, subjects)

print("\nExam Timetable:")

for subject, time in solution.items():
    print(subject, "->", time)

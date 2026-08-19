# ============================================================
# EXPERIMENT 15
# PERSON DOB KNOWLEDGE BASE
# ============================================================

print("==============================================")
print("          PERSON DOB KNOWLEDGE BASE")
print("==============================================")

# ------------------------------------------------------------
# Knowledge Base - Person and Date of Birth Facts
# ------------------------------------------------------------

persons = {
    "John": "15-05-2002",
    "Priya": "20-08-2003",
    "Arun": "10-12-2001",
    "Meena": "25-03-2004",
    "Divya": "19-08-2003"
}

# ------------------------------------------------------------
# Display stored facts
# ------------------------------------------------------------

print("\nStored Person DOB Records:")

for name, dob in persons.items():
    print("Person :", name, " | DOB :", dob)

# ------------------------------------------------------------
# Query the Knowledge Base
# ------------------------------------------------------------

print("\n==============================================")
print("             DOB QUERY SYSTEM")
print("==============================================")

name = input("Enter person's name: ")

# ------------------------------------------------------------
# Rule-based logical reasoning
# ------------------------------------------------------------

if name in persons:
    dob = persons[name]

    print("\n==============================================")
    print("             PERSON DETAILS")
    print("==============================================")

    print("Person Name      :", name)
    print("Date of Birth    :", dob)

    print("\nLogical Reasoning:")
    print("IF person exists in the knowledge base")
    print("THEN retrieve the corresponding date of birth.")

else:
    print("\n==============================================")
    print("             RECORD NOT FOUND")
    print("==============================================")

    print("No DOB record found for", name)

# ------------------------------------------------------------
# End of Program
# ------------------------------------------------------------

print("\n==============================================")
print("DOB retrieved using rule-based reasoning.")
print("==============================================")
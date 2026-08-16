from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier

data = [
    ["young", "low", "no", "no"],
    ["young", "high", "no", "yes"],
    ["middle", "low", "yes", "yes"],
    ["old", "low", "yes", "yes"],
    ["old", "high", "no", "no"]
]

x, y = [], []

enc = [LabelEncoder() for i in range(3)]

for i in range(3):
    enc[i].fit([r[i] for r in data])

for r in data:
    x.append([enc[i].transform([r[i]])[0] for i in range(3)])
    y.append(r[3])

model = DecisionTreeClassifier(
    criterion="entropy",
    max_depth=3
)

model.fit(x, y)

print("DECISION TREE")

print("Features:", ["Age", "Income", "Existing Loan"])

new = [["middle", "high", "no"]]

new = [
    enc[i].transform([new[0][i]])[0]
    for i in range(3)
]

print("Loan Decision:", model.predict([new])[0])

# ============================================================
# EXPERIMENT 14
# DIET RECOMMENDATION EXPERT SYSTEM
# ============================================================

print("==============================================")
print("       DIET RECOMMENDATION EXPERT SYSTEM")
print("==============================================")

# Get user information
age = int(input("Enter your age: "))
bmi = float(input("Enter your BMI: "))

print("\nSelect your health condition:")
print("1. Diabetes")
print("2. High Blood Pressure")
print("3. High Cholesterol")
print("4. None")

condition = int(input("Enter your choice (1-4): "))

# ------------------------------------------------------------
# Rule-based expert system
# ------------------------------------------------------------

if bmi < 18.5:
    bmi_category = "Underweight"
elif bmi < 25:
    bmi_category = "Normal weight"
elif bmi < 30:
    bmi_category = "Overweight"
else:
    bmi_category = "Obese"

# Diet recommendation rules

if condition == 1:
    health_condition = "Diabetes"

    diet = [
        "Choose whole grains such as oats and brown rice",
        "Eat plenty of vegetables",
        "Choose low-sugar fruits in moderate portions",
        "Include protein such as beans, eggs and fish",
        "Avoid sugary drinks and sweets"
    ]

elif condition == 2:
    health_condition = "High Blood Pressure"

    diet = [
        "Eat plenty of fresh vegetables and fruits",
        "Choose whole grains",
        "Include low-fat dairy products",
        "Choose fish, beans and lean protein",
        "Reduce salt and processed foods"
    ]

elif condition == 3:
    health_condition = "High Cholesterol"

    diet = [
        "Eat oats and other high-fiber foods",
        "Include vegetables and fruits",
        "Choose beans and legumes",
        "Choose fish and other lean proteins",
        "Limit foods high in saturated fat"
    ]
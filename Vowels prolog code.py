# ============================================================
# EXPERIMENT
# VOWEL IDENTIFICATION USING RULE-BASED LOGIC
# ============================================================

print("==============================================")
print("       VOWEL IDENTIFICATION SYSTEM")
print("==============================================")

# Get input sentence
sentence = input("Enter a sentence: ")

# ------------------------------------------------------------
# Rule-based vowel identification
# ------------------------------------------------------------

vowels = "aeiouAEIOU"

vowel_list = []
consonant_list = []
other_list = []

for char in sentence:

    # Rule 1: Check whether character is a vowel
    if char in vowels:
        vowel_list.append(char)

    # Rule 2: Check whether character is an alphabet
    elif char.isalpha():
        consonant_list.append(char)

    # Rule 3: Other characters such as space, number, symbol
    else:
        other_list.append(char)

# ------------------------------------------------------------
# Display result
# ------------------------------------------------------------

print("\n==============================================")
print("              CLASSIFICATION")
print("==============================================")

print("Original Sentence :", sentence)

print("\nVowels:")
if vowel_list:
    print(vowel_list)
else:
    print("No vowels found")

print("\nConsonants:")
if consonant_list:
    print(consonant_list)
else:
    print("No consonants found")

print("\nOther Characters:")
if other_list:
    print(other_list)
else:
    print("No other characters found")

print("\n==============================================")
print("Character classification completed using")
print("rule-based logic.")
print("==============================================")
# FIND-S Algorithm

data = [
    ["Sunny", "Warm", "Normal", "Strong", "Warm", "Same", "Yes"],
    ["Sunny", "Warm", "High",   "Strong", "Warm", "Same", "Yes"],
    ["Rainy", "Cold", "High",   "Strong", "Warm", "Change", "No"],
    ["Sunny", "Warm", "High",   "Strong", "Cool", "Change", "Yes"]
]

# Initial hypothesis: most specific
hypothesis = ["Ø"] * 6

print("FIND-S Algorithm")
print("----------------")

for row in data:
    attributes = row[:-1]
    target = row[-1]

    # FIND-S considers only positive examples
    if target == "Yes":
        if hypothesis == ["Ø"] * 6:
            hypothesis = attributes.copy()
        else:
            for i in range(len(hypothesis)):
                if hypothesis[i] != attributes[i]:
                    hypothesis[i] = "?"

        print("After example:", row)
        print("Hypothesis  :", hypothesis)

print("\nFinal Most Specific Hypothesis:")
print(hypothesis)

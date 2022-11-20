# Jump Statement

# Break Statement

lst = ["raja", "rani", "joker", "chor", "police", "mantri"]
for nm in lst:
    if nm == "chor":
        break
    print(nm)

# Continue Statement

for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i)

# Pass Statement

lst = ["raja", "rani", "joker", "chor", "police", "mantri"]
for nm in lst:
    pass
print(nm)

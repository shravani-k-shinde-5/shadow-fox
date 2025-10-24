vidhi_expenses = {
    "Hotel": 1200,
    "Food": 800,
    "Transportation": 500,
    "Attractions": 300,
    "Miscellaneous": 200
}

my_expenses = {
    "Hotel": 1000,
    "Food": 900,
    "Transportation": 600,
    "Attractions": 400,
    "Miscellaneous": 150
}

vidhi_total = sum(vidhi_expenses.values())
my_total = sum(my_expenses.values())

print(f"Vidhi's total expenses: ${vidhi_total}")
print(f"My total expenses: ${my_total}")

if vidhi_total > my_total:
    print("Vidhi spent more overall.")
elif my_total > vidhi_total:
    print("I spent more overall.")
else:
    print("Vidhi and I spent the same amount.")

max_diff = 0
max_diff_category = ""

for category in vidhi_expenses:
    diff = abs(vidhi_expenses[category] - my_expenses[category])
    if diff > max_diff:
        max_diff = diff
        max_diff_category = category

print(f"The category with the most significant spending difference is '{max_diff_category}' with a difference of ${max_diff}.")

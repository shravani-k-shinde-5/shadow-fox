import random

no_6 = 0
no_double_6 = 0
no_ones = 0

rows_6 = 0
rolls = 20
for i in range(rolls):
    roll = random.randint(1, 6)
    if roll == 6:
        no_6 += 1
        if rows_6 == 1:
            no_double_6 += 1
        rows_6 = 1
    else:
        rows_6 = 0
    if roll == 1:
        no_ones += 1

print("how many times you rolled six :", no_6)
print("how many times you rolled six in rows:", no_double_6)
print("how many times you rolled one :", no_ones)

  
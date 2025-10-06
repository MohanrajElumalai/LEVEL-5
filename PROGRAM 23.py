rows = 5

for i in range(1, rows + 1):
    print(" " * (i - 1) + "*")


print("*" * rows)


for i in range(rows - 1, 0, -1):
    print(" " * (i - 1) + "*")

M = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

col2 = [row[1] for row in M]
print(col2)

col2_plus_one = [row[1] + 1 for row in M]  # Add 1 to each item in column 2
print(col2_plus_one)

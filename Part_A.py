Die_A = [1, 2, 3, 4, 5, 6]
Die_B = [1, 2, 3, 4, 5, 6]

# 1
total_combinations = len(Die_A) * len(Die_B)
print("Total combinations:", total_combinations)

# 2
combination_distribution = [[0] * 6 for _ in range(6)]

for i in range(6):
    for j in range(6):
        combination_distribution[i][j] = Die_A[i] + Die_B[j]

print("Distribution of possible combinations:")
for row in combination_distribution:
    print(row)

# 3
sum_count = {}

for row in combination_distribution:
    for sum_value in row:
        if sum_value in sum_count:
            sum_count[sum_value] += 1
        else:
            sum_count[sum_value] = 1

probabilities = {sum_value: count / total_combinations for sum_value, count in sum_count.items()}

print("Probability of each possible sum (rounded to 2 decimal places):")
for sum_value, probability in probabilities.items():
    print(f"P(Sum = {sum_value}) = {probability:.2f}")

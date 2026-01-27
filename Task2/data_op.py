# data_op.py

numbers = [5, 2, 9, 1, 5, 6]

# Remove duplicates
unique_numbers = list(set(numbers))

# Sort
unique_numbers.sort()

# Max, Min, Average
maximum = max(unique_numbers)
minimum = min(unique_numbers)
average = sum(unique_numbers) / len(unique_numbers)

print("Unique Sorted Numbers:", unique_numbers)
print("Max:", maximum)
print("Min:", minimum)
print("Average:", average)

# List comprehension
squares = [x*x for x in unique_numbers]
print("Squares:", squares)

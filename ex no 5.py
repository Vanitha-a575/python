import pandas as pd
from functools import reduce

# Sample data: list of numbers
numbers = [5, 12, 7, 20, 3]

# Convert list to pandas Series
data = pd.Series(numbers)

# Filter: select numbers greater than 10
filtered_data = data[data > 10]
print("Numbers > 10:", list(filtered_data))

# Map: multiply each number by 2 using apply()
def multiply_by_2(x):
    return x * 2

mapped_data = filtered_data.apply(multiply_by_2)
print("Numbers after multiplying by 2:", list(mapped_data))

# Apply: add 5 to each number (simulated with apply())
def add_5(x):
    return x + 5

applied_data = mapped_data.apply(add_5)
print("Numbers after adding 5:", list(applied_data))

# Reduce: sum all numbers using reduce
def sum_two(x, y):
    return x + y

total = reduce(sum_two, applied_data)
print("Total sum:", total)


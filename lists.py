'''

Basic list operations

'''

nums = [0, 1, 2, 3, 4, 5]
print(nums)         # [0, 1, 2, 3, 4, 5]
print(nums[1:4])    # [1, 2, 3]
print(nums[::2])    # [0, 2, 4] (every 2nd element)
print(nums[::-1])   # [5, 4, 3, 2, 1, 0] (reverse)

fruits = ["apple", "banana", "cherry"]
fruits[1] = "blueberry"  # Change 2nd element
fruits.append("orange")  # Add to end
fruits.insert(1, "mango")  # Insert at index 1
fruits.remove("apple")    # Remove by value
popped = fruits.pop(2)   # Remove & return by index

'''
List comprehension
[expression for item in iterable if condition]
'''
squares = [x**2 for x in range(5)]
# Result: [0, 1, 4, 9, 16]

evens = [x for x in range(10) if x % 2 == 0]
# Result: [0, 2, 4, 6, 8]

words = ["hello", "world", "python"]
upper_words = [word.upper() for word in words]
# Result: ["HELLO", "WORLD", "PYTHON"]

'''
Exercise
- 1. Create a list of squares from 1 to 10.
- 2. Filter vowels from a string.
- 3. Flatten a 2D list (convert to 1D).
'''

numbers = range(1,11)
squares = [number * number for number in numbers]
print(f"List of squares: {squares}")  # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

str = "hellow world"
vowels = "aeiou"
filtered_vowels = [x for x in str if x in vowels]
print(f"Filtered vowels: {filtered_vowels}")

two_d_list = [[1, 2, 3], [4, 5], [6]]
flattened_list = [item for sublist in two_d_list for item in sublist]
print(f"Flattened list: {flattened_list}")

# Size of list
example_list = [1, 2, 3]
print(len(example_list))

# Looping through a list
fruits = ['apple', 'banana', 'cherry']

for fruit in fruits:
    print(fruit)

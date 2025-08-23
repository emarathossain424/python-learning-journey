"""
Sets are an unordered collection of unique elements in Python.

"""

empty_set = set()
print(empty_set)    # Output: set()

fruits = {"apple", "banana", "cherry"}
# Output: {"apple", "banana", "cherry"}
print(fruits)

fruits = {"banana", "cherry", "date","banana"}
# Output: {"banana", "cherry", "date"} - After removing duplication
print(f"After removing duplication - {fruits}")       



# Basic Set operations

s = {1,2,3}

# Add an element
s.add(4) 

# Add multiple elements
s.update([5,6])

# Remove an element,
# But will raise error if not found
s.remove(2)       

# Remove an element, but won't raise error if not found
s.discard(3)      

# Remove and return an arbitrary element
poped = s.pop()      

# Clear all elements, and output set()
clear_set = s.clear()

# Advance set operations

a = {1,2,3,4}
b = {3,4,5,6}

# Union
print(a | b)          # Output: {1, 2, 3, 4, 5, 6}
print(a.union(b))     # Output: {1, 2, 3, 4, 5, 6}

# Intersection
print(a & b)          # Output: {3, 4}
print(a.intersection(b)) # Output: {3, 4}

# Difference
print(a - b)          # Output: {1, 2}
print(a.difference(b))# Output: {1, 2}

# Symmetric Difference
print(a ^ b)          # Output: {1, 2, 5, 6}
print(a.symmetric_difference(b)) # Output: {1, 2, 5, 6}

is_subset = a.issubset(b)  # Check if a is subset of b
is_superset = a.issuperset(b)  # Check if a is superset of b
is_disjoint = a.isdisjoint(b)  # Check if a and b have no elements in common

# Size of sets
fruits = {"apple", "banana", "cherry"}
print(len(fruits))  # Output: 3

# Looping through a set

set_of_fruits = {'apple','banana','orange'}

for fruit in set_of_fruits:
    print(fruit)
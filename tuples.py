'''
What is a Tuple?
A tuple is a fundamental data structure in Python (and many other programming languages)
that is used to store an ordered, finite sequence of elements. The key characteristics of
a tuple are:

1. Ordered: The items have a defined order, and that order will not change.
You access elements by their position (index).

2. Immutable: Once a tuple is created, it cannot be changed. 
You cannot add, remove, or modify elements after creation. This is the main difference between a tuple and a list.

3. Heterogeneous: While not a strict rule, tuples are typically used to store collections of
different data types, representing a single logical entity (like a database record). 
Lists are often used for homogeneous items.

4. Indexable & Iterable: You can access elements by their index (e.g., my_tuple[0])
and loop through them with a for loop.

'''

my_tuple = (1,2,3,4,5)
print(my_tuple)

# Parentheses are optional, but the comma is what defines it.
another_tuple = "apple", "banana", 42
print(another_tuple)  # Output: ('apple', 'banana', 42)

# A single-element tuple needs a trailing comma
single_element_tuple = ("hello",)
print(single_element_tuple)  # Output: ('hello',)
print(type(single_element_tuple))  # Output: <class 'tuple'>

# Without the comma, it's just a string in parentheses
not_a_tuple = ("hello")
print(type(not_a_tuple))  # Output: <class 'str'>

# Key Operations with Tuples
# 1. Accessing Elements (Indexing & Slicing)

my_tuple = (10, 20, 30, 40, 50)

# Accessing elements
print(my_tuple[0])  # Output: 10
print(my_tuple[1:4])  # Output: (20, 30, 40)
print(my_tuple[-1])  # Output: 50 (last element)

# 2. Immutability in Action
my_tuple = (1, 2, 3)
# my_tuple[1] = 20  # This line will cause a TypeError: 'tuple' object does not support item assignment

# 3. Unpacking 
# This is a very powerful and convenient feature.
# You can assign the elements of a tuple to variables in a single statement.

person = ("Alice", 30, "Engineer")
name, age, profession = person # Unpacking

print(name)        # Output: Alice
print(age)         # Output: 30
print(profession)  # Output: Engineer

# 4. Concatenation and Repetition

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

# Concatenation
combined = tuple1 + tuple2
print(combined)  # Output: (1, 2, 3, 4, 5, 6)

# Repetition
tuple3 = ('hello',)
repeated = tuple3 * 2
print(repeated)  # Output: ('hello', 'hello')

# Size of tuple
print(len(tuple1))  # Output: 3
print(len(tuple2))  # Output: 3
print(len(tuple3))  # Output: 1

# Looping through tuple

tuple4 = (7,8,9,10)
for item in tuple4:
    print(item)
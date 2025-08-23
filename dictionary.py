'''
What is a Dictionary?
A dictionary (type dict) is a collection of key-value pairs. It's:

    - Unordered (In Python 3.7+, it is ordered, but it's best to think of it as unordered for general purposes. The order is a implementation detail you shouldn't rely on for logic).

    - Mutable: You can change, add, and remove items after creation.

    - Indexed by Keys: You don't use numerical indices like [0]. You use unique keys to access their associated values.

    - No Duplicate Keys: Each key must be unique. If you assign a value to an existing key, it overwrites the old value.

'''

my_dict = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

print(my_dict)  # Output: {'name': 'Alice', 'age': 30, 'city': 'New York'}

my_dict_2 = dict(name="Bob", age=25, city="Los Angeles")

print(my_dict_2)  # Output: {'name': 'Bob', 'age': 25, 'city': 'Los Angeles'}

# Basic Operations: Accessing, Adding, Changing, Removing
# 1. Accessing Values

my_dict_3 = {
    "name": "Charlie",
    "age": 35,
    "city": "Chicago"
}

print(my_dict_3["name"])  # Output: Charlie
print(my_dict_3.get("name"))  # Output: 35

print(my_dict_3["age"])  # Output: 35
print(my_dict_3.get("age"))  # Output: 35

print(my_dict_3["city"])  # Output: Chicago
print(my_dict_3.get("city"))  # Output: Chicago

# 2. Adding and Changing Values

my_dict_3["age"] = 36  # Change existing value
my_dict_3["email"] = "charlie@example.com"  # Add new key-value pair

print(my_dict_3)

# 3. Removing itemes

my_dict_4 = { "name": "David", "age": 40, "city": "Miami" }

val = my_dict_4.pop("age")  # Remove by key and return it's value
print(f"Removed age: {val}")  # Output: Removed age: 40

val2 = my_dict_4.popitem()  # Remove and return last inserted key-value pair
print(f"Removed item: {val2}") # prints Removed item: ('city', 'Miami'), as a tuple

my_dict_4.clear() # Clearing whole dictionary
print(my_dict_4)  # Output: {}

# Looping through a dictionary

my_dict_5 = {
    "name": "Eve",
    "age": 45,
    "city": "Seattle"
}

# Looping through keys
for key in my_dict_5:
    print(key)

# Looping through values
for value in my_dict_5.values():
    print(value)

# Looping through key-value pairs
for key, value in my_dict_5.items():
    print(f"{key}: {value}")

# Checking for Existence
my_dict = {"name": "Alice", "age": 30}
print("name" in my_dict)   # Output: True
print("job" in my_dict)    # Output: False

def log_and_make_odd(func):
    # This is a decorator function.
    # A decorator is used to add extra features to another function without changing its code.
    def wrapper(*args, **kwargs):
        # This code runs before the original function.
        print(f"Calling function: {func.__name__}")
        result = func(*args, **kwargs)  # Call the original function.
        
        # This code runs after the original function.
        print(f"Function {func.__name__} returned: {result}")
        
        # If result is even, return the closest smaller odd number
        if isinstance(result, int) and result % 2 == 0:
            return result - 1
        return result
    return wrapper  # Return the new function with extra features.

@log_and_make_odd  # Apply the decorator
def add(a, b):
    """Add two numbers."""
    print(f"Adding {a} and {b}")
    sum = a + b
    return sum

output = add(5, 3)
print(f"Result: {output}")
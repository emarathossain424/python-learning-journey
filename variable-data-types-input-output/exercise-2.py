# ✅ Exercise 2:
# Take two numbers as input and print their:

# Sum

# Difference

# Product

# Taking first number as input and setting it in the variable number_one
number_one = input( "Please enter first number - " )
# Parsing string to float
number_one = float(number_one)

# Taking second number as input and setting it in the variable number_two
number_two = input("Please enter second number - ")
# Parsing string to float
number_two = float(number_two)

sum = number_one + number_two
difference = number_one - number_two
product = number_one * number_two

print("Sum: ", sum)
print("Difference: ", difference)
print("Product: ", product)
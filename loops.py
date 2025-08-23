'''
Question 1 — Multiplication Table with a For Loop
Ask the user for a number n.

Print the multiplication table for n from 1 × n up to 10 × n.

Use a for loop with range() for this.

Example: if n = 3

python-repl
Copy
Edit
3 x 1 = 3
3 x 2 = 6
...
3 x 10 = 30

'''
def multiplication_table(n):
    
    # Here range(1, 11) generates numbers from 1 to 10.
    # range(10) would generate numbers from 0 to 9.
    # range(1,11,3) would generate numbers from 1 to 10, 
    # but only include every 3rd number (1, 4, 7, 10).
    for i in range(1,11):
        print(f"{n} x {i} = {n*i}")

multiplication_table(3)


'''
Question 2 — Guess the Number with a While Loop
The program randomly chooses a number between 1 and 50.

The user keeps guessing until they get it right.

After each guess:

If guess is too low → print "Too low! Try again."

If guess is too high → print "Too high! Try again."

When guessed correctly → print "Correct! You guessed it in X tries."

Use a while loop for this.
'''

choosed_number = 25  # This would be randomly chosen in a real scenario
tries = 0

user_input = int(input("Guess a number between 1 and 50: "))

while (choosed_number != user_input):
    tries += 1
    if(user_input < choosed_number):
        print("Too low! Try again.")
    elif(user_input > choosed_number):
        print("Too high! Try again.")
    user_input = int(input("Guess another number between 1 and 50: "))

print(f"Correct! you guessed it in {tries} tries.")

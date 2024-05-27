# Nested If-Else Statement Example

meaning = 100  # Initial value assigned to the variable 'meaning'

# Nested if-else statement to check multiple conditions
if meaning > 50:
    if meaning > 75:
        print("Meaning is greater than 75")  # This block executes if both conditions are True
    else:
        print("Meaning is greater than 50 but less than or equal to 75")  # This block executes if the first condition is True and the second is False
else:
    print("Meaning is less than or equal to 50")  # This block executes if the first condition is False

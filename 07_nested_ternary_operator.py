# Nested Ternary Conditional Operator Example

meaning = 100  # Initial value assigned to the variable 'meaning'

# Nested ternary conditional statement to check multiple conditions
print("Meaning is greater than 75") if meaning > 75 else print("Meaning is greater than 50 but less than or equal to 75") if meaning > 50 else print("Meaning is less than or equal to 50")
# This single line of code is equivalent to the nested if-else statement:
# if meaning > 75:
#     print("Meaning is greater than 75")
# elif meaning > 50:
#     print("Meaning is greater than 50 but less than or equal to 75")
# else:
#     print("Meaning is less than or equal to 50")

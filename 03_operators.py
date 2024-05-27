# Python Operators

# Arithmetic Operators
print("Arithmetic Operators")
print(2 + 2)      # Addition: 2 + 2 = 4
print(10 - 4)     # Subtraction: 10 - 4 = 6
print(10 / 5)     # Division: 10 / 5 = 2.0 (results in a float)
print(2 * 5)      # Multiplication: 2 * 5 = 10
print(10 // 2)    # Floor Division: 10 // 2 = 5 (results in an integer)
print(10 % 2)     # Modulus: 10 % 2 = 0 (remainder of the division)
print(round(10 / 2))  # Rounding: round(10 / 2) = 5 (rounds the result)

# Assignment Operators
meaning = 10
print("Assignment Operators")
print(meaning)        # Initial value: 10
meaning += 1
print(meaning)        # Addition assignment: meaning += 1 (meaning = meaning + 1) = 11
meaning -= 1
print(meaning)        # Subtraction assignment: meaning -= 1 (meaning = meaning - 1) = 10
meaning *= 12
print(meaning)        # Multiplication assignment: meaning *= 12 (meaning = meaning * 12) = 120
meaning /= 2
print(meaning)        # Division assignment: meaning /= 2 (meaning = meaning / 2) = 60.0
meaning %= 3
print(meaning)        # Modulus assignment: meaning %= 3 (meaning = meaning % 3) = 0.0

# Additional Operators

# Exponentiation Operator
print("Exponentiation Operator")
print(2 ** 3)    # Exponentiation: 2 ** 3 = 8 (2 raised to the power of 3)

# Bitwise Operators
print("Bitwise Operators")
print(4 & 5)     # AND: 4 & 5 = 4 (binary AND operation)
print(4 | 5)     # OR: 4 | 5 = 5 (binary OR operation)
print(4 ^ 5)     # XOR: 4 ^ 5 = 1 (binary XOR operation)
print(~4)        # NOT: ~4 = -5 (binary ones' complement)
print(4 << 1)    # Left Shift: 4 << 1 = 8 (shift bits to the left)
print(4 >> 1)    # Right Shift: 4 >> 1 = 2 (shift bits to the right)

# Comparison Operators
print("Comparison Operators")
print(10 == 10)  # Equal to: 10 == 10 is True
print(10 != 5)   # Not equal to: 10 != 5 is True
print(10 > 5)    # Greater than: 10 > 5 is True
print(10 < 15)   # Less than: 10 < 15 is True
print(10 >= 10)  # Greater than or equal to: 10 >= 10 is True
print(10 <= 15)  # Less than or equal to: 10 <= 15 is True

# Logical Operators
print("Logical Operators")
print(True and False)  # Logical AND: True and False is False
print(True or False)   # Logical OR: True or False is True
print(not True)        # Logical NOT: not True is False

# Identity Operators
print("Identity Operators")
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print(x is z)  # is: x is z is True (both variables point to the same object)
print(x is y)  # is: x is y is False (different objects with same content)
print(x == y)  # ==: x == y is True (same content)

# Membership Operators
print("Membership Operators")
print("apple" in x)  # in: "apple" in x is True (checks if "apple" is in the list x)
print("pear" not in x)  # not in: "pear" not in x is True (checks if "pear" is not in the list x)

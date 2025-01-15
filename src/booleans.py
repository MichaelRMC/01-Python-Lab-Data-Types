# Task 1: Complex Boolean Expressions
# -----------------------------------
# Evaluate the following boolean expressions:
# 1. (10 > 5) and (5 <= 3) or (100 == 100)
#
# 2. not (7 != 7) or ((3 < 2) and (4 == 4))
#
# 3. (4 ** 2 > 15) and ((100 / 10) < 9) or (5 == 5 and not (10 == 10))
#

# Write the answers in comments below each expression and print the results.
print(True)
print(False)
print(False)
# Task 2: Boolean Function
# ------------------------
# Write a Python function that takes two numbers as input and returns True if the first number is divisible by the second, and False otherwise.


def is_divisible(x, y):
    # Your code here
    return bool(x % y == 0)

# Task 3: Complex Logical Operations
# ----------------------------------
# Write a Python function that evaluates whether a given integer is:
# 1. Positive, even, and divisible by 3.
# 2. Negative, odd, and greater than -10.


def complex_check(n):
    # Your code here
    x = (n > 0) and (n % 2 == 0) and (n % 3 != 0)
    y = (n > 0) and (n % 2 == 1) and (n > -10)
    return n == x or n == y


# Task 4: Boolean Type Conversion
# -------------------------------
# Convert the following expressions to booleans using the `bool()` function and explain the results:
# 1. 0 
# 2. 3.14
# 3. -100
# 4. ""
# 5. "False"
# 6. []

# Use the `bool()` function and print the results with comments explaining the outcomes.
print(bool(0))  # => 0 is a false value.
print(bool(3.14))  # => 3.14 is a true value.
print(bool(-100))  # => -100 is a true value.
print(bool(""))  # => An empty string is a false value.
print(bool("False"))  # => A string is a true value.
print(bool([]))  # => An empty list is a false value.
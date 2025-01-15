# mixed_operations.py

# Task 1: Combined Operations
# ---------------------------
# Evaluate the following complex expressions:
# 1. (3 + 5 * 2) > (10 / 2) and (not (4 == 4) or 7 % 2 == 1)
# 2. "Data" * 3 + "Science" > "DataScience"
# 3. 100 > 50 and "Code" == "code".upper()

# Write the answers in comments below each expression and print the results.

# Task 2: Type Conversion and Operations
# --------------------------------------
# Write a Python function that takes an integer and a string representing a number (e.g., "25") and:
# 1. Converts the string to an integer and adds it to the original integer.
# 2. Converts the sum back to a string and concatenates it with the original string.
# 3. Returns the final result.

def combine_and_convert(num, num_str):
    # Your code here
    convert_num_str = int(num_str)
    sum = num+convert_num_str
    sum_str = str(sum)
    return sum_str + num_str

# Task 3: Mixed Type Handling
# ---------------------------
# Write a Python function that takes two parameters, a number and a boolean, and:
# 1. Returns the number squared if the boolean is True.
# 2. Returns the square root of the number if the boolean is False.

def mixed_operations(num, flag):
    # Your code here
    pass

# Task 4: Data Type Comparison
# ----------------------------
# Write a Python function that compares the data types of two inputs and returns True if they are the same, and False otherwise.

def compare_types(a, b):
    a_type = type(a)
    b_type = type(b)
    if a_type != b_type:
        return False
    else:
        return True

# 1. Division by Zero
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print("Example 1 Error Raised:", type(e).__name__, f"({e})")

# 2. Invalid String Arithmetic
try:
    result = "Python" - "Code"
except TypeError as e:
    print("Example 2 Error Raised:", type(e).__name__, f"({e})")

# 3. Arithmetic with None
try:
    result = None + 10
except TypeError as e:
    print("Example 3 Error Raised:", type(e).__name__, f"({e})")
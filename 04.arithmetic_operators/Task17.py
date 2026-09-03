# Testing string operations
text1 = "Hello"
text2 = "World"
count = 3

# 1. string + string
try:
    print("string + string: ", text1 + text2)
except TypeError as e:
    print("string + string Error:", e)

# 2. string - string
try:
    print("string - string: ", text1 - text2)
except TypeError as e:
    print("string - string Error:", e)

# 3. string * integer
try:
    print("string * integer:", text1 * count)
except TypeError as e:
    print("string * integer Error:", e)

# 4. string / string
try:
    print("string / string: ", text1 / text2)
except TypeError as e:
    print("string / string Error:", e)
    
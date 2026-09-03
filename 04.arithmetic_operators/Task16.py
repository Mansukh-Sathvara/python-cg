# Create a string and repeat it using an integer
word = "Python"
repeated_word = word * 3
print("String multiplied by int (3):", repeated_word)

# Attempt to multiply a string by a float
try:
    result_float = word * 2.5
except TypeError as e:
    print("Error when multiplying by float:", e)
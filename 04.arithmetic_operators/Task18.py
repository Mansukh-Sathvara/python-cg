value = None

operations = [
    ("Addition", lambda: value + 5),
    ("Subtraction", lambda: value - 5),
    ("Multiplication", lambda: value * 5),
    ("Division", lambda: value / 5),
    ("Floor Division", lambda: value // 5),
    ("Modulus", lambda: value % 5),
    ("Exponentiation", lambda: value ** 5),
]

for name, op in operations:
    try:
        op()
    except TypeError as e:
        print(f"{name:15}: TypeError -> {e}")
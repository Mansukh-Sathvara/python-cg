a = 10
b = -3
c = 2.5

expressions = [
    ("a + b", 7, a + b),
    ("a * c", 25.0, a * c),
    ("a / b", -3.3333333333333335, a / b),
    ("a // b", -4, a // b),
    ("a % b", -2, a % b),
    ("b ** 2", 9, b ** 2),
    ("a + b * c", 2.5, a + b * c),
    ("(a + b) * c", 17.5, (a + b) * c),
    ("a - b ** 2 / c", 6.4, a - b ** 2 / c),
    ("a // c + a % b", 2.0, a // c + a % b)
]

for expr_str, predicted, actual in expressions:
    match_status = "Match" if predicted == actual else "Mismatch"
    print(f"Expr: {expr_str:15} | Predicted: {str(predicted):20} | Python: {str(actual):20} | {match_status}")
    
# Task 13 — Arithmetic with Booleans

# Addition
add_res = True + False
# Subtraction
sub_res = True - False
# Multiplication
mul_res = True * False
# Division (True / True to avoid ZeroDivisionError with False)
div_res = True / True
# Floor division
fdiv_res = True // True
# Modulus
mod_res = True % True
# Exponentiation
pow_res = True ** False

print("Addition (True + False):       ", add_res, "  | Type:", type(add_res))
print("Subtraction (True - False):    ", sub_res, "  | Type:", type(sub_res))
print("Multiplication (True * False): ", mul_res, "  | Type:", type(mul_res))
print("Division (True / True):        ", div_res, "| Type:", type(div_res))
print("Floor Division (True // True): ", fdiv_res, "  | Type:", type(fdiv_res))
print("Modulus (True % True):         ", mod_res, "  | Type:", type(mod_res))
print("Exponentiation (True ** False):", pow_res, "  | Type:", type(pow_res))
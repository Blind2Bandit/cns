import math

def crt_readable(remainders, moduli):
    M = math.prod(moduli)    
    total_sum = 0

    for rem, mod in zip(remainders, moduli):

        partial_product = M // mod
        inverse = pow(partial_product, -1, mod)
        
        # 5. Multiply the remainder, partial product, and inverse together
        term = rem * partial_product * inverse
        
        # 6. Add it to our running total
        total_sum += term
        
    # 7. The final answer is the total sum modulo M
    return total_sum % M

# --- Usage ---
# We want a number x where:
# x % 3 = 2
# x % 5 = 3
# x % 7 = 2
result = crt_readable([2, 3, 2], [3, 5, 7])
print(f"The solution is x = {result}")
# Jennifer Ly, grudat20 uppg 1.1

def factorial(n):
    """Check faculty."""
    fact = 1
    for numb in range(2,n+1):
        fact *= numb
    return fact

# Unit test
assert factorial(0) == 1
assert factorial(1) == 1
assert factorial(3) == 6
assert factorial(6) == 720
assert factorial(10) == 3628800

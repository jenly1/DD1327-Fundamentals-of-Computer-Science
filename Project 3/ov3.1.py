# Jennifer Ly, grudat20 uppg 3.1

# Recursive faculty function
def factorial(n):
    return 1 if (n == 0) else n * factorial(n-1)

# Unit test
assert factorial(0) == 1
assert factorial(1) == 1
assert factorial(3) == 6
assert factorial(6) == 720
assert factorial(10) == 3628800 

########################################## Proof through mathematical induction ##########################################
""" 
Base case: P(0) is true since the function returns 1 when n = 0.

Inductive step: “P(i) is true for all i < k”, i.e. the call factorial(n) returns i * (i-1) * ... * 4 * 3 * 2 * 1 * 1 = 
(i^2 - i) * ... * 4 * 3 * 2 * 1 * 1, when i < k. Using this hypothesis, we need to prove P(k). The call factorial(k) will 
return k * factorial(k-1), where factorial(k-1) returns (k-1) * ... * 4 * 3 * 2 * 1 * 1. Ergo, factorial(k) will return:

k(k-1) * ... * 4 * 3 * 2 * 1 * 1) = (k^2 - k) * ... * 4 * 3 * 2 * 1 * 1, Q.E.D

"""
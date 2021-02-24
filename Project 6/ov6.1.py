# Jennifer Ly, grudat20 uppg 6.1

import time

# Function that calculates the maximume revenue by recursion 
# O(2^n)
def p(n):
    # Creates the given h-vector 
    h1 = [0, 2, 5, 6, 9]
    h2 = (n-4)*[0]
    h = h1 + h2

    # Calculates the maximume revenue  
    revenue = []
    if n==0:                         # base-case
        return 0
    else:
        for i in range(1, n+1):      # must start from 1 for recursion to work, otherwise wants to enter p(1) when calculating p(1) (for example)              
            numb = h[i]+p(n-i)
            revenue.append(numb)
        return max(revenue)           

# Unit test 
assert p(0) == 0
assert p(1) == 2
assert p(2) == 5
assert p(3) == 7
assert p(4) == 10
assert p(5) == 12

# Task: Explain why the time complexity is exponential 
# Answer: The recursive call ignites that the algorithm's growth doubles with each additon to the input.
# This can easily be visualized by drawing a tree over all the function calls.

########################################## MEMOIZATION ##############################################

# Function that calculates the maximume revenue by caching
# O(n^2)
cache = {}      
def p_memo(n):
    # Creates the given h-vector 
    h1 = [0, 2, 5, 6, 9]
    h2 = (n-4)*[0]
    h = h1 + h2 

    # Calculates the maximume revenue  
    if n in cache.keys():                   # checks if value haven't already been calculated
        return cache[n]
    if n==0:
        return 0
    else:
        revenue = []
        for i in range(1, n+1):                        
            numb = h[i]+p_memo(n-i)
            revenue.append(numb)
        cache[n] = max(revenue)              # saves the new value in the dictionary, where key=n and value=maximume revenue 
    return max(revenue)
    
# Unit test 
assert p_memo(0) == 0
assert p_memo(1) == 2
assert p_memo(2) == 5
assert p_memo(3) == 7
assert p_memo(4) == 10
assert p_memo(5) == 12

# Calculates the running time for both functions to demostrate the time difference
start = time.time()
p(10)
print("Running time 1:", time.time() - start)

start = time.time()
p_memo(10)
print("Running time 2:", time.time() - start)
# Jennifer Ly, grudat20 upppg 3.3

import random

# Creates vector with randomized elements
def vector(length, lowerbound, upperbound):
    vec = []
    for i in range(0, length):
        i = random.randint(lowerbound, upperbound)
        vec.append(i) 
    return vec

# Segregates the vector into negative elements and positive elements 
# O(n) time complexity, O(1) extra space
def segregate(vector):
    j = 0                                   
    for i in range(len(vector)): 
        # Invariant: If the current element vector[i] is negative, we'll replace it with vector[j], where index j is in 
        # range[0, amount of negative numbers] 
        if vector[i] < 0:                   # if number in list is less than 0
            temp = vector[i]                # negative number is temporarily put in a variable
            vector[i] = vector[j]           # negative number at index i will be replaced by random number at index j
            vector[j] = temp                # random number at index j will be replaced by negative number at index i
            j = j+1                         # j is a counter that depends on the amount of negative numbers in the list
    return vector

def test(vector, j):
    segregate(vector)
    i = 0
    for i in range(len(vector)):
        if i <= j:
            assert vector[i] < 0
        else:
            assert vector[i] >= 0
    return vector

def main():
    vec1 = vector(10, -5, 5)
    vec2 = vector(10, -10, 10)
    vec3 = vector(10, -100, 100)
    print("Vector 1 sorted:", segregate(vec1))
    print("Vector 2 sorted:", segregate(vec2))
    print("Vector 3 sorted:", segregate(vec3))
    

main()

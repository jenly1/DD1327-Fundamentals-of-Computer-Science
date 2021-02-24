# Jennifer Ly, grudat20 upppg 4.2

import random

# Sorts elements in list
# O(n+k)
def sortedlist(A, k): 
    # A=unsorted list with values x1,x2,...,xn
    # For every value of xi, following applies: 0 ≤ xi ≤ k

    # Createst a list B that will serve as temporary memory and a list C that will be the sorted list
    B = [0]*(k+1)
    C = [0]*len(A)

    # Counts the digits in A and puts the number in C
    # O(n)
    for i in range(0, len(A)):
        digit = A[i]
        B[digit] = B[digit] + 1 

    # Modifies B
    # O(k)
    for i in range(1, len(B)):
        B[i] = B[i] + B[i-1]

    # Adds digits from A to B by using values in C as index
    # O(n)
    for i in range(0, len(A)):
        digit = A[i]
        B[digit] = B[digit] - 1
        C[B[digit]] = A[i]
    return C

# Creates a vector with randomized elements 
def vec(length, randmax):
    vec = []
    for i in range(0, length):
        i = random.randint(0, randmax)
        vec.append(i) 
    return vec
    
def main():
    # Creates vectors
    vec1 = vec(10,5)
    vec2 = vec(10,10)
    vec3 = vec(10,20)

    # Sorts vectors
    vec1sort = sortedlist(vec1,5)
    vec2sort = sortedlist(vec2,10)
    vec3sort = sortedlist(vec3,20)

    # Visualizes the result
    print("Vector 1 sorted:", vec1sort)
    print("Vector 2 sorted:", vec2sort)
    print("Vector 3 sorted:", vec3sort)

main()

# Question: For what values of k makes sortedlist() linear?
# Answer: If k=n.
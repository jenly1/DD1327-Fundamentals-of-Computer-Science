# Jennifer Ly, grudat20 uppg. 3.2

import random

# Creates a vector with randomized elements 
def vector(length, randmax):
    vec = []
    for i in range(0, length):
        i = random.randint(0, randmax)
        vec.append(i) 
    return vec

# Calculates the mode
# O(n)
def mode(vector):
    counts = {}                                  # key=number, value=amount of times the number appears
    lst = []                                     
    maxcount = 0                                 # maxcount=mode

    for number in vector:                       
        if number not in counts:
            counts[number] = 0                   # if first time encountering this number, assert the value to zero
        counts[number] += 1                      # add 1 to the value
        if counts[number] > maxcount:
            maxcount = counts[number]            

    if maxcount != 1:                            # if several modes, return lowest number 
        for number, count in counts.items():     
            if count == maxcount:       
                lst.append(number)                  
        return min(lst)                          # min()=built in function with O(n) time complexity
    else:                           
        return None                              # if no mode, return None
                          

def main():
    vec1 = vector(10, 5)
    vec2 = vector(10, 10)
    vec3 = vector(10, 50)
    print("Mode 1:", mode(vec1), "| Vector 1:", vec1)
    print("Mode 2:", mode(vec2), "| Vector 2:", vec2)
    print("Mode 3:", mode(vec3), "| Vector 3:", vec3)
    

main()